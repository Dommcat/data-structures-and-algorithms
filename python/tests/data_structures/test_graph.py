import pytest
from data_structures.graph import Graph, Vertex, Edge, Node

def test_exists():
    assert Graph

# Test 1: Node can be successfully added to the graph
# @pytest.mark.skip("TODO")
def test_add_node():
    graph = Graph()
    expected = "spam"
    actual = graph.add_node("spam").value
    assert actual == expected

# Test 2: An edge can be successfully added to the graph
# @pytest.mark.skip("TODO")
def test_add_edge():
    graph = Graph()
    node_a = graph.add_node("A")
    node_b = graph.add_node("B")
    graph.add_edge(node_a, node_b, 1)
    edge = graph.adjacency_list[node_a][0]
    assert edge.vertex == node_b
    assert edge.weight == 1

# Test 3: A collection of all nodes can be properly retrieved from the graph
# @pytest.mark.skip("TODO")
def test_get_nodes():
    graph = Graph()
    node_a = graph.add_node("A")
    node_b = graph.add_node("B")
    nodes = graph.get_nodes()
    assert node_a in nodes
    assert node_b in nodes

# Test 4: All appropriate neighbors can be retrieved from the graph
# @pytest.mark.skip("TODO")
def test_get_neighbors():
    graph = Graph()
    node_a = graph.add_node("A")
    node_b = graph.add_node("B")
    graph.add_edge(node_a, node_b, 1)
    neighbors = graph.get_neighbors(node_a)
    assert len(neighbors) == 1
    assert neighbors[0].vertex == node_b

# Test 5: Neighbors are returned with the weight between nodes included
# @pytest.mark.skip("TODO")
def test_neighbors_weight():
    graph = Graph()
    node_a = graph.add_node("A")
    node_b = graph.add_node("B")
    graph.add_edge(node_a, node_b, 1)
    neighbors = graph.get_neighbors(node_a)
    assert neighbors[0].weight == 1

# Test 6: The proper size is returned, representing the number of nodes in the graph
# @pytest.mark.skip("TODO")
def test_size():
    graph = Graph()
    graph.add_node("A")
    graph.add_node("B")
    assert graph.size() == 2


# Test 7: A graph with only one node and edge can be properly returned
# @pytest.mark.skip("TODO")
def test_single_node_edge():
    graph = Graph()
    node_a = graph.add_node("A")
    graph.add_edge(node_a, node_a, 1)
    neighbors = graph.get_neighbors(node_a)
    assert len(neighbors) == 1
    assert neighbors[0].vertex == node_a









# Unused tests below 


# # Test 8:
# # @pytest.mark.skip("TODO")
# def test_bouquet():
#     g = Graph()
#     apple = g.add_node("apple")
#     g.add_edge(apple, apple, 10)
#     neighbors = g.get_neighbors(apple)
#     assert len(neighbors) == 1
#     assert neighbors[0].vertex.value == "apple"
#     assert neighbors[0].weight == 10


# # Test 9:
# def test_add_edge_interloper_start():
#     graph = Graph()
#     node_a = graph.add_node("A")
#     interloper = Vertex("Interloper")

#     with pytest.raises(ValueError, match="Both vertices must be in the graph"):
#         graph.add_edge(interloper, node_a)


# # @pytest.mark.skip("TODO")
# def test_add_edge_interloper_end():

#     graph = Graph()

#     end = Vertex("end")

#     start = graph.add_node("start")

#     with pytest.raises(KeyError):
#         graph.add_edge(start, end)

# @pytest.mark.skip("TODO")
# def test_size_empty():

#     graph = Graph()

#     expected = 0

#     actual = graph.size()

#     assert actual == expected

# @pytest.mark.skip("TODO")
# def test_size():

#     graph = Graph()

#     graph.add_node("spam")

#     expected = 1

#     actual = graph.size()

#     assert actual == expected
