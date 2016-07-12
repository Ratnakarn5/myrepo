class Dog():
	def quack(self):
		print("Dog don't quack")
	def walk(self):
		print("Walk like  dog")
	def bark(self):
		print("Wooff")
	def fur(self):
		print("Black fur")

class Duck():
	def quack(self):
		print("quack")
	def walk(self):
		print("Walk like  duck")
	def bark(self):
		print("Don't bark")
	def fur(self):
		print("don't have fur")

def in_the_forest(dog): #can except any object that has fur and bark methods
	dog.fur()
	dog.bark()

def in_the_pond(duck):
	duck.quack()
	duck.walk()


def main():
	donald = Duck()
	fido = Dog()
	#polymorphism
	in_the_forest(donald)
	in_the_pond(fido)
	#normal useage
	# for i in (donald, fido):
	# 	i.quack()
	# 	i.walk()
	# 	i.bark()
	# 	i.fur()

if __name__ == '__main__':main()

	