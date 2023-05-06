class Node:
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return f"Node({self.value})"

class Edge:
    def __init__(self, vertex, weight=1):
        self.vertex = vertex
        self.weight = weight

    def add_edge(self, vertex1, vertex2, weight=1):
        """
        Add edge
        Arguments: 2 vertices to be connected by the edge, weight (optional)
        Adds a new edge between two vertices in the graph
        If specified, assign a weight to the edge
        Both vertices should already be in the Graph
        """
        if vertex1 not in self.adjacency_list or vertex2 not in self.adjacency_list:
            raise ValueError("Both vertices must be in the graph")

        edge = Edge(vertex2, weight)
        self.adjacency_list[vertex1].append(edge)

class Graph:
    def __init__(self):
        self.adjacency_list = {}

    def add_node(self, value):
        """
        add vertex
        Arguments: value
        Add a vertx to the graph
        :return: added vertex
        """
        new_vertex = Vertex(value)
        self.adjacency_list[new_vertex] = []
        return new_vertex

    def add_edge(self, vertex1, vertex2, weight=1):
        if vertex1 not in self.adjacency_list or vertex2 not in self.adjacency_list:
            raise ValueError("Both vertices must be in the graph")

        edge = Edge(vertex2, weight)
        self.adjacency_list[vertex1].append(edge)

    def get_nodes(self):
        return list(self.adjacency_list.keys())

    def get_neighbors(self, vertex):
        return self.adjacency_list[vertex]

    def size(self):
        return len(self.adjacency_list)

class Vertex:
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return f"Vertex({self.value})"


