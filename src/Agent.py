class Agent:
	def __init__(self, graph, x, y):
		self.graph = graph
		self.position = (x, y)

	def get_position(self):
		return self.position