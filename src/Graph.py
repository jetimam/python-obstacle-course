import random

class Graph:
	def __init__(self, width):
		self.width = width
		self.array = []
		self.OBSTACLE_RATE = 5 # this means there will be 1 obstacle per 5 columns
		self.obstacle_amount = width // self.OBSTACLE_RATE

	def initialize(self):
		for i in range(0, self.width):
			self.array.append([])

			rand = []
			for x in range(self.obstacle_amount):
				rand.append(random.randrange(0, self.width))
				
			for j in range(0, self.width):
				if j in rand:
					self.array[i].append(0)
				else:
					self.array[i].append(1)
		self.array[1][2] = 2

	def draw(self):
		for i in range(self.width):
			print(self.array[i])

	def get_spawn_point(self):
		rand = random.randint(0,1) #finding a random edge, either left or right
		if rand == 0:
			x = 0
		else:
			x = self.width-1
		
		run = True
		while run: #finding a legal position on that edge
			rand = random.randint(0, self.width-1)
			if self.array[x][rand] == 1:
				y = rand
				run = False
		
		return (x, y)

	def get_destination(self, spawn_edge):

		if spawn_edge == 0: #finding the opposite edge
			x = self.width-1
		else:
			x = 0
		
		run = True
		while run: #finding a legal position on that edge
			rand = random.randint(0, self.width-1)
			if self.array[x][rand] == 1:
				y = rand
				run = False
		
		return (x, y)

	def obstacle_check(self):
		for i in range(self.width):
			for j in range(self.width):
				print('(', i , ',' , j, ') is:' , self.array[i][j])