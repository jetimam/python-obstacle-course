import Graph, Agent

graph = Graph.Graph(5)
graph.initialize()
graph.draw()

print('--------------------')

spawn_point = graph.get_spawn_point()
agent = Agent.Agent(graph, spawn_point[0], spawn_point[1])
print(agent.get_position())