#creates a class called object.
class Bike(object):
	#attributes of the bike
	def __init__(self,price, max_speed, miles):
		self.price = price
		self.max_speed = max_speed
		self.miles = 0

	#creates a method which displays the bikes info. 
	#remember python cannot concatenate strings and integers. Use the str() function to turn integers into strings. 
	def display_info(self):
		print "Price:" + " " + str(self.price)
		print "Maximum Speed" + " " + str(self.max_speed)
		print "Miles" + " " + str(self.miles)

	#method that adds 10
	def ride(self):
		self.miles += 10

	#method that takes away 5 from the total miles. 
	def reverse(self):
		if self.miles >= 5:
			self.miles -= 5

#sets instance of class with sets variables. 
bike_red = Bike(150,50,10)
bike_red.ride()
bike_red.ride()
bike_red.ride()
bike_red.reverse()
bike_red.display_info()

bike_blue = Bike(250,75,30)
bike_blue.ride()
bike_blue.ride()
bike_blue.reverse()
bike_blue.reverse()
bike_blue.display_info()

bike_yellow = Bike(99,100,30)
bike_yellow.reverse()
bike_yellow.reverse()
bike_yellow.reverse()
bike_yellow.display_info()

