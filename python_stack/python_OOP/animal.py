
#BE SURE TO CAPITALIZE ALL CLASS NAMES!
class Animal(object):
	def __init__(self,name,health):
		self.name = name
		self.health = health

	def walk(self):
		self.health -= 1
		return self

	def run(self):
		self.health -= 5
		return self

	def display_health(self):
		print self.health
		return self

animal1 = Animal("Kong", 40)
animal1.walk()
animal1.walk()
animal1.walk()
animal1.run()
animal1.run()
animal1.display_health()

#or 
#it can be written like so.
animal1 = Animal("Kong", 40).walk().walk().walk().run().run().display_health()

class Dog(Animal):
	def __init__(self):
		super(Dog,self).__init__("dog",150)
		self.health = 150

	def pet(self):
		self.health += 5
		return self

class Dragon(Animal):
	def __init__(self):
		super(Dragon,self).__init__("dragon",170)

	def fly(self):
		self.health -= 10

	def displayHealth(self):
		super(Dragon,self).display_health()
		print "I am a dragon"
		return self


animal2 = Dog()
animal2.walk()
animal2.walk()
animal2.walk()
animal2.run()
animal2.run()
animal2.pet()
animal2.display_health()

animal3 = Dragon()
animal3.fly()
animal3.fly()
animal3.displayHealth()

#animal 2 cannot fly because it is inheriting from Animal and not Dragon subclass.
#animal2.fly()
#animal2.display_health9()




