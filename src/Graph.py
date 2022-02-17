import random

class Graph:
	def __init__(self, width):
		self.width = width
		self.array = [[]]
		self.OBSTACLERATE = 5 # this means there will be 1 obstacle per 5 columns
		self.obstacleAmount = width // self.OBSTACLERATE

	def initialize(self):
		for i in range(0, self.width):
			self.array.append([])

			rand = []
			for x in range(self.obstacleAmount):
				rand.append(random.randrange(0, self.width))
				
			for j in range(0, self.width):
				if j in rand:
					self.array[i].append(0)
				else:
					self.array[i].append(1)
		self.array.pop()

	def draw(self):
		for i in range(self.width):
			print(self.array[i])