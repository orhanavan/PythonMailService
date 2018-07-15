# inheritance
class Animal():
	noise = "Grunt"
	size = "Large"
	color = "Brown"
	hair = "Covers body"

	def get_color(self):
		return self.color

	def make_noise(self):
		return self.noise

class Dog(Animal):
	name = "Jon"
	
jon = Dog()
jon.color = "white"
jon.name = "Jon Snow"

print(Dog.hair)