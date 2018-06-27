class product(object):
	def __init__(self,price,name,weight,brand,status):
		self.price = price
		self.name = name
		self.weight = weight
		self.brand = brand
		self.status = "for sale!"
	
	#Returning self from a method simply means that your method,
	#returns a reference to the instance object o which it was called. 	
	def sell(self):
		self.status = "Sold!"
		return self


	def add_tax(self,tax):
		 return self.price * .20
		

	def returns(self,reason):
		if reason == "Defective":
			self.price = 0
		elif reason == "Like new":
			self.status = "for sale!"
		elif reason == "Opened":
			self.status = "Used"
			discount = self.price * .20
			self.price - discount
		return self

	def display_info(self):
		print "The price is" + " " + str(self.price)
		print "The name of this item is" + " " + self.name
		print "This item weighs" + " " + str(self.weight)
		print "The brand is" + " " + self.brand
		print "This item is " +  self.status


product1 = product(15,"deodorant","20z","Kiss My Face",15)

product1.display_info()
product1.add_tax(.20)
product1.sell()
product1.display_info()
product1.returns("Opened")
product1.display_info()

product2 = product(25,"Genmaicha","150z","Argo Tea","for sale")
product2.display_info()
product2.returns("Defective")
product2.display_info()
