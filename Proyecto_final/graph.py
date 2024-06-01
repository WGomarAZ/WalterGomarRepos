class UndirectedGraph:
    def __init__(self):
        self.graph_dict = {}

    def add_vertex(self, vertex):
        if vertex in self.graph_dict:
            return "Vertex already in graph"
        self.graph_dict[vertex] = []

    def add_edge(self, vertex1, vertex2, value=0):
        if vertex1 not in self.graph_dict or vertex2 not in self.graph_dict:
            raise ValueError("One or both vertices not found in graph")
        edge = Edge(vertex1, vertex2, value)
        self.graph_dict[vertex1].append(edge)
        self.graph_dict[vertex2].append(Edge(vertex2, vertex1, value))

    def is_vertex_in(self, vertex):
        return vertex in self.graph_dict

    def get_vertex(self, vertex_name):
        for v in self.graph_dict:
            if vertex_name == v.get_name():
                return v
        print(f"Vertex {vertex_name} does not exist")

    def get_neighbours(self, vertex):
        return self.graph_dict[vertex]

    def __str__(self):
        all_edges = ""
        for v1 in self.graph_dict:
            for edge in self.graph_dict[v1]:
                all_edges += f"{v1} --({edge.get_value()})--> {edge.get_v2()}\n"
        return all_edges


class Edge:
    def __init__(self, v1, v2, value=0):
        self.v1 = v1
        self.v2 = v2
        self.value = value

    def get_value(self):
        return self.value

    def set_value(self, value):
        self.value = value

    def get_v1(self):
        return self.v1

    def get_v2(self):
        return self.v2

    def __str__(self):
        return f"{self.v1} --({self.value})--> {self.v2}"


# Representing a Tic-Tac-Toe game state as a dictionary
initial_state = {"board": [["", "", ""], ["", "", ""], ["", "", ""]], "player": "X"}

graph = UndirectedGraph()
graph.add_vertex(initial_state)
print(graph)
