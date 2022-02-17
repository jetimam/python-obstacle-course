import random

class Graph:
	def __init__(self, width):
		self.width = width
		self.array = [[]]

	def initialize(self):
		for i in range(0, self.width):
			self.array.append([])
			rand = random.randrange(0, self.width)
			for j in range(0, self.width):
				if j == rand:
					self.array[i].append(0)
				else:
					self.array[i].append(1)
		self.array.pop()

	def draw(self):
		for i in range(self.width):
			print(self.array[i])