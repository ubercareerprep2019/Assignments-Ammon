# Graphs - Ex1
from collections import deque


class GraphNode:
	def __init__(self, data):
		self.data = data


class GraphWithAdjacencyList:
	def __init__(self):
		self.__adj_nodes = {}
		self.__nodes = {}

	def add_node(self, key: int):
		g_key = GraphNode(key)
		self.__nodes[key] = g_key
		self.__adj_nodes[g_key] = []

	def remove_node(self, key: int):
		if key in self.__nodes:
			g_key = self.__nodes[key]
			del self.__nodes[key]
			del self.__adj_nodes[g_key]

	def add_edge(self, node1: int, node2: int):
		if node1 in self.__nodes and node2 in self.__nodes:
			g_node1 = self.__nodes[node1]
			g_node2 = self.__nodes[node2]

			self.__adj_nodes[g_node1].append(g_node2)
			self.__adj_nodes[g_node2].append(g_node1)

	def remove_edge(self, node1: int, node2: int):
		if node1 in self.__nodes and node2 in self.__nodes:
			g_node1 = self.__nodes[node1]
			g_node2 = self.__nodes[node2]

			self.__adj_nodes[g_node1].remove(g_node2)
			self.__adj_nodes[g_node2].remove(g_node1)

	def get_adj_nodes(self, key: int):
		g_key = self.__nodes[key]
		if g_key not in self.__adj_nodes:
			return []
		return self.__adj_nodes[g_key]


graph = GraphWithAdjacencyList()
# Tests for the Graph.

# graph.add_node(5)
# graph.add_node(19)
# graph.add_node(12)
# graph.remove_node(19)
# graph.add_edge(5,12)
# graph.add_edge(18, 7)
# graph.remove_edge(19,2)
# graph.remove_node(901)
# [print(i.data) for i in graph.get_adj_nodes(5)]
# graph.remove_edge(12,5)


graph.add_node(2)
graph.add_node(0)
graph.add_node(1)
graph.add_node(3)

graph.add_edge(2,0)
graph.add_edge(2,3)
graph.add_edge(2,1)
graph.add_edge(0,1)


# Graphs - Ex2


def get_dfs(start_node_data, visited=set()):
	print(start_node_data)

	visited.add(start_node_data)
	adj_list = graph.get_adj_nodes(start_node_data)

	for node in adj_list:
		if node.data not in visited:
			get_dfs(node.data)


# print("DFS starting at 2")
# get_dfs(2)


# Graphs - Ex3


def get_bfs(start_node_data):
	queue = deque([start_node_data])
	visited = set()

	while queue:
		node_data = queue.popleft()

		if node_data not in visited:
			visited.add(node_data)
			print(node_data)
			adj_list = graph.get_adj_nodes(node_data)
			queue.extend([_node.data for _node in adj_list])


# print("BFS starting at 2")
# get_bfs(2)