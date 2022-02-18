class Agent:
	def __init__(self, graph, spawn_point, destination_point):
		self.graph = graph
		self.position = (spawn_point[0], spawn_point[1])
		self.destination = (destination_point[0], destination_point[1])


	def get_position(self):
		return self.position

	def get_destination(self):
		return self.destination