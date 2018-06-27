class car(object):
	def __init__(self,price,speed,fuel,mileage):
		self.price = price
		self.speed = speed
		self.fuel = fuel
		self.mileage = mileage

	def display_all(self):
		if self.fuel == 0:
			self.fuel = "Empty"
		elif self.fuel <= 50 and self.fuel >= 0:
			self.fuel = "Half Full"
		else:
			self.fuel = "Full"
		tax = 0
		if self.price > 10000:
			tax = 0.15
		else:
			tax = 0.12

		print "The price of this car is" + " " + str(self.price)
		print "It's top speed is" + " " + str(self.speed) + " " + "mph"
		print "The fuel is" + " " + str(self.fuel) 
		print "It has" + " " + str(self.mileage) 
		print tax

car_black = car(15000,215,25,100000)
car_black.display_all()

car_red = car(3000,150,88,89000)
car_red.display_all()

car_green = car(8900,200,15,65000)
car_green.display_all()

car_yellow_sport = car(200000,285,100,5)
car_yellow_sport.display_all()

car_silver = car(9999,250,20,10000)
car_silver.display_all()

car_maroon = car(20000,200,100,20000)
car_maroon.display_all()
