import matplotlib.pyplot as plt

class Planet:
	def __init__(self):
		self.population = 100
		self.birth_rate = 1.1
		self.death_rate = 1.02
		self.population_list = []
		self.total_resources = 1000
		self.total_resources_list = []
			

	def step(self):
		self.population *= self.birth_rate
		ratio = self.population/self.total_resources
		if ratio > 1.3:
			self.population /= ratio
		self.population_list.append(self.population)


	def render(self):
		plt.plot(self.population_list, c="blue")