import Graph, Agent

graph = Graph.Graph(5)
graph.initialize()
graph.draw()

print('--------------------')

spawn_point = graph.get_spawn_point()
destination = graph.get_destination(spawn_point[0])

agent = Agent.Agent(graph, spawn_point, destination)
print(agent.get_position(), agent.get_destination())