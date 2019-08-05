from collections import deque
from part3 import GraphWithAdjacencyList


# Graphs - ex4
def get_initial_graph_ex4():
	graph = GraphWithAdjacencyList()

	# Nodes
	graph.add_node(0)
	graph.add_node(1)
	graph.add_node(2)
	graph.add_node(3)
	graph.add_node(4)
	graph.add_node(5)
	graph.add_node(6)

	# Edges
	graph.add_edge(0, 1)
	graph.add_edge(0, 2)
	graph.add_edge(0, 4)
	graph.add_edge(1, 2)
	graph.add_edge(2, 5)
	graph.add_edge(3, 4)
	graph.add_edge(4, 5)
	graph.add_edge(4, 6)

	return graph


def min_number_of_edges(node1, node2):
	graph = get_initial_graph_ex4()

	queue = deque([node1])

	while queue:
		node_data = queue.popleft()
		adj_list = graph.get_adj_nodes(node_data)

