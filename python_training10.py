class Animal():
	name = "Amy"
	noise = "Grunt"
	size = "Large"
	color = "Brown"
	hair = "Covers body"

	def get_color(self, abc):
		return self.color + " " + abc
		# dog self'e karşılık gelir, abc boşta kalır
		# ama sorun oluşturmaz, referansı olan bir nesne olarak kullanılır
	@property	
	def make_noise(self):
		return self.noise
		# property sayesinde methodu kullanırken parantez kullanmaya gerek kalmıyor
		
"""
dog = Animal()
print(dog.get_color("red"))
print(dog.make_noise)
"""
def write_anything():
	print("Just anything..")