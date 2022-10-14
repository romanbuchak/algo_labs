import copy
import sys

INT_MAX = sys.maxsize


class Graph:

    def __init__(self) -> None:
        self.nodes = set()
        self.edges = {}
        self.distances = {}

    def add_node(self, node: int) -> None:
        self.nodes.add(node)

    def add_edge(self, from_node: int, to_node: int, distance=INT_MAX) -> None:
        self.add_node(from_node)
        self.add_node(to_node)
        self.edges.setdefault(from_node, set()).add(to_node)
        self.distances[from_node, to_node] = distance

    def add_two_sided_edge(self, from_node: int, to_node: int, distance=INT_MAX) -> None:
        self.add_edge(from_node, to_node, distance)
        self.add_edge(to_node, from_node, distance)

    def dijkstra(self, current_node: int) -> dict:
        max_distance_length = INT_MAX
        distances_to_nodes = {current_node: 0}
        unchecked_nodes = copy.deepcopy(self.nodes)

        while unchecked_nodes:
            closest_node = INT_MAX

            for node in distances_to_nodes:
                if node in unchecked_nodes and node < closest_node:
                    closest_node = node
                    break
            unchecked_nodes.remove(closest_node)

            for neighbour_node in self.edges[closest_node]:
                distance_to_closest_node = distances_to_nodes.get(closest_node) +\
                                           self.distances[closest_node, neighbour_node]
                if neighbour_node not in distances_to_nodes.keys() or\
                        (distances_to_nodes[neighbour_node] > distance_to_closest_node and
                         max_distance_length >= distance_to_closest_node):
                    distances_to_nodes[neighbour_node] = distance_to_closest_node

        return distances_to_nodes