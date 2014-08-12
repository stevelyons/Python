## Animal is a object (yes, sort of confusing) look at extra credit
class Animal(object):
	pass

## ??
class Dog(Animal):

	def __init__(self, name):
		## ??
		self.name = name

## ?? 
class Cat(Animal):

	def __init__(self, name):
		## ?? 
		self.name = name

## ??
class Person(object):
	def __init__(self, name):
		## Person has-a pet of some kind
		self.pet = None
	## function Person object name
	def printName(name):
		print "My name is %s", name 

## ?? 
class Employee(Person):

	def __init__(self, name, salary):
		## ?? hmm what is this strange magic?
		super(Employee, self).__init__(name)
		## ??
		self.salary = salary

## ??
class Fish(object):
	pass

## ??
class Salmon(Fish):
	pass

## ?? 
class Halibut(Fish):
	pass

## function
def printPetName(self, name):
	print self.name 

## rover is-a Dog
rover = Dog("Rover")

## satan is-a Cat
satan = Cat("Satan")

## mary is-a Person
mary = Person("Mary")

## mary has-a pet "satan"
mary.pet = satan

## frank is-a employee
frank = Employee("Frank", 120000)

## frank has a pet rover
frank.pet = rover

## flipper is an instance of the object Fish
flipper = Fish()

## crouse is an instance of the object Salmon; which is dervied from Cat
crouse = Salmon()

## ??
harry = Halibut()

# print Mary's name
mary.printName()
