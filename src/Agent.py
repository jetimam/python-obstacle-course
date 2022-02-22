from queue import Queue

class Agent:
	def __init__(self, graph, spawn_point, destination_point):
		self.graph = graph
		self.spawn_point = (spawn_point[0], spawn_point[1])
		self.destination = (destination_point[0], destination_point[1])


	def get_spawn_point(self):
		return self.spawn_point

	def get_destination(self):
		return self.destination

	def find_destination_BFS(self):
		queue = Queue(0)
		backtracking_table = {}
		visited = []
		found = False

		queue.put(self.spawn_point)
		visited.append(self.spawn_point)

		while not found:
			current_cell = queue.get()

			if current_cell == self.destination:
				found = True
			else:
				children = self.generate_children(current_cell, visited)

				for child in children:
					visited.append(child)
					queue.put(child)
					backtracking_table[child] = current_cell

		return self.back_track(current_cell, backtracking_table)

	def generate_children(self, current_cell, visited):
		children = []

		# the outer ifs are checking if we are on the borders, the inner ifs are checking if the neighbors are 1s
		if current_cell[0] != self.graph.width-1: #going right
			if self.graph.array[current_cell[0] + 1][current_cell[1]] == 1 and (current_cell[0] + 1, current_cell[1]) not in visited:
				children.append((current_cell[0] + 1, current_cell[1]))
		if current_cell[0] != 0: #going left
			if self.graph.array[current_cell[0] - 1][current_cell[1]] == 1 and (current_cell[0] - 1, current_cell[1]) not in visited:
				children.append((current_cell[0] - 1, current_cell[1]))
		if current_cell[1] != self.graph.width-1: #going down
			if self.graph.array[current_cell[0]][current_cell[1] + 1] == 1 and (current_cell[0], current_cell[1] + 1) not in visited:
				children.append((current_cell[0], current_cell[1] + 1))
		if current_cell[1] != 0: #going up
			if self.graph.array[current_cell[0]][current_cell[1] - 1] == 1 and (current_cell[0], current_cell[1] - 1) not in visited:
				children.append((current_cell[0], current_cell[1] - 1))

		return children

	def back_track(self, current_cell, backtracking_table):
		path = []

		path.append(current_cell)
		while current_cell != self.spawn_point:
			path.append(backtracking_table[current_cell])
			current_cell = backtracking_table[current_cell]

		path.reverse()
		return path