class Dog():
	name = "Jon"
	color = "Brown"

	def get_color(self):
		return self.color

obj = Dog()
print(obj.get_color())