from ast import If
from queue import Queue

class Agent:
	def __init__(self, graph, spawn_point, destination_point):
		self.graph = graph
		self.position = (spawn_point[0], spawn_point[1])
		self.destination = (destination_point[0], destination_point[1])


	def get_position(self):
		return self.position

	def get_destination(self):
		return self.destination

	def find_destination_BFS(self):
		queue = Queue(0)
		backtracking_table = {}
		visited = []
		found = False
		queue.put(self.position)
		visited.append(self.position)

		while not found:
			current_cell = queue.get()

			if current_cell == self.destination:
				found = True
			else:
				children = self.generate_children(current_cell, visited)

				for child in children:
					if child not in visited:
						visited.append(child)
						queue.put(child)
						backtracking_table[child] = current_cell

		return self.back_track(current_cell, backtracking_table)

	def generate_children(self, current_cell, visited):
		children = []

		if self.graph[current_cell[0] + 1][current_cell[1]] == 1 and (current_cell[0]+1, current_cell[1]) not in visited:
			children.append((current_cell[0] + 1, current_cell[1])) #going right
		if self.graph[current_cell[0]][current_cell[1] + 1] == 1 and (current_cell[0], current_cell[1] + 1) not in visited:
			children.append((current_cell[0], current_cell[1] + 1)) #going up
		if self.graph[current_cell[0]][current_cell[1] - 1] == 1 and (current_cell[0], current_cell[1] - 1) not in visited:
			children.append((current_cell[0], current_cell[1] - 1)) #going down
		if self.graph[current_cell[0] - 1][current_cell[1]] == 1 and (current_cell[0] - 1, current_cell[1]) not in visited:
			children.append((current_cell[0] - 1, current_cell[1])) #going left

		return children

	def back_track(self, current_cell, backtracking_table):
		path = []

		while current_cell != self.position:
			path.append(backtracking_table[current_cell])
			current_cell = backtracking_table[current_cell]

		return path.reverse()