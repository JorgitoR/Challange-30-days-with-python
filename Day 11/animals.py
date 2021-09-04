class Animal:
	noise = "Arrr"
	color = "Red"

	def noise(self):
		print(self.noise)

	def make_noise(self, new_noise):
		self.noise = new_noise

	def get_noise(self):
		return self.noise

	def get_color(self):
		return self.color 

	def set_color(self, new_color):
		self.color = new_color
		return self.color 


class Wolf(Animal):
	noise ="grrr"

class BabyWolf(Wolf):
	color="Yellow"
