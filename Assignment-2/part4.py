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
	nodes_visited = set()
	distance_to_node = {node1: 0}
	while queue:
		node_data = queue.popleft()
		if node_data not in nodes_visited:
			if node_data == node2:
				return distance_to_node[node_data]

			nodes_visited.add(node_data)
			adj_list = graph.get_adj_nodes(node_data)

			unvisited_adj_list = [
				node.data
				for node in adj_list
				if node.data not in nodes_visited
			]

			for node in unvisited_adj_list:
				if node not in distance_to_node:
					distance_to_node[node] = distance_to_node[node_data] + 1
			queue.extend(unvisited_adj_list)

	return None


# print(min_number_of_edges(1,5))
# print(min_number_of_edges(6,1))
# print(min_number_of_edges(6,5))
# print(min_number_of_edges(6,6))


# Graphs - ex5

def nb_of_islands(island_map):
	if not island_map:
		return "Invalid Grid"

	visited_map = [
		[False for _ in range(len(island_map[0]))] for _ in range(len(island_map))
	]

	islands = 0
	for i, row in enumerate(island_map):
		for j, col_val in enumerate(row):
			if col_val == 1 and not visited_map[i][j]:
				get_neighbors(i, j, island_map, visited_map)
				islands += 1
	return "1, All the ‘1’s can be connected to form a single island." \
		if islands == 1 \
		else \
		str(islands) + ", there are " + str(islands) + " disconnected islands in this map."


def get_neighbors(i, j, island_map, visited_map):
	if is_valid(i, j, island_map, visited_map):
		visited_map[i][j] = True

		get_neighbors(i - 1, j, island_map, visited_map)
		get_neighbors(i + 1, j, island_map, visited_map)
		get_neighbors(i, j - 1, island_map, visited_map)
		get_neighbors(i, j + 1, island_map, visited_map)


def is_valid(i, j, island_map, visited_map):
	num_cols, num_rows = len(island_map[0]), len(island_map)
	if 0 <= i < num_rows and 0 <= j < num_cols:
		if island_map[i][j] == 1 and not visited_map[i][j]:
			return True
	return False


print(nb_of_islands([
	[1, 1, 1, 1, 0],
	[1, 1, 0, 1, 0],
	[1, 1, 0, 0, 0],
	[0, 0, 0, 0, 0]
]))

print(nb_of_islands([
	[1, 1, 0, 0, 0],
	[1, 1, 0, 0, 0],
	[0, 0, 1, 0, 0],
	[0, 0, 0, 1, 1]
]))
