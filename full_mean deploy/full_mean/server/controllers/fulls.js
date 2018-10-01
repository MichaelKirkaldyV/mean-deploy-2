var mongoose = require('mongoose');
var User = mongoose.model('User') // We are retrieving this Schemas from our Models
const bcrypt = require('bcryptjs');

module.exports = {

	//Finds all Authors on Homepage.
	login: function(req, res) {
    	User.findOne({username: req.body.username}, function(err, user){
        if(err) {
            console.log("can't login");
        } 
        else {
            if(user){
                const entered_password = req.body.password;
                const hashed_password = user.password;

                //compares password from login form to the hashed password saved into the db.
                //If passwords are correct, set sessions to id and username.
                bcrypt.compare(entered_password, hashed_password, function(err, correctpass) {
                    if(correctpass) {
                        console.log("You're logged in!");
                        req.session.username = user.username;
                        req.session.userid = user._id;
                        //check if the user is logged in
                        req.session.isloggedin = true;
                    } 
                    else {
                        console.log("Incorrect password! Try again.");
                    } 
                });
            } 
            else {
                console.log("User does not exist.");
            } 
        } 
    })
    },

    register: function(req, res) {
        var form_password = req.body.password;
        console.log("In Regisration controller")

        //Hashes password
        bcrypt.hash(form_password, 10, function(err, hash) {
        if(err) {
            console.log(err);
        } 
        else {
            var user = new User({username: req.body.username, password: hash });
         }
        }); //End of bycrpt
        user.save(function(err, data){
             if(err){
                console.log("We have an error!", err);
            }
            else {
                console.log(data);
                console.log('successfully added a user!');
                res.json(data)
            }
        }); //end of save
    }
}; //End of exports