class Person:

	# init method or constructor
	def __init__(self, name):
		self.name = name

	
	def say_hi(self):
		print('Hello, my name is', self.name)


p = Person('Srinivasan ')
p.say_hi()

p1= Person('Angelica')
p1.say_hi()