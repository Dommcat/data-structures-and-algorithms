# Python 401: Code Challenge Class 35
## Graphs

## Whiteboard Process:
<!-- Embedded whiteboard image -->
 <!-- [WhiteBoard Code Challenge 12](wbcc12animal.png) -->
N/A
<!--
[//]: # (## Approach & Efficiency)

[//]: # (What approach did you take? Why? What is the Big O space/time for this approach?) -->


## Features:

Implement your own Graph. The graph should be represented as an adjacency list, and should include the following methods:

add node
Arguments: value
Returns: The added node
Add a node to the graph
add edge
Arguments: 2 nodes to be connected by the edge, weight (optional)
Returns: nothing
Adds a new edge between two nodes in the graph
If specified, assign a weight to the edge
Both nodes should already be in the Graph
get nodes
Arguments: none
Returns all of the nodes in the graph as a collection (set, list, or similar)
Empty collection returned if there are no nodes
get neighbors
Arguments: node
Returns a collection of edges connected to the given node
Include the weight of the connection in the returned collection
Empty collection returned if there are no nodes
size
Arguments: none
Returns the total number of nodes in the graph
0 if there are none


## Solution Code:
<!-- Show how to run your code, and examples of it in action -->

[Code Challenge 35 - Code Example](/python/data_structures/graph.py)

## Code Re/Sources:
ChatGPT

Class Demo File

## Testing:

feature tests to prove the following functionality:

- Node can be successfully added to the graph
- An edge can be successfully added to the graph
- A collection of all nodes can be properly retrieved from the graph
- All appropriate neighbors can be retrieved from the graph
- Neighbors are returned with the weight between nodes included
- The proper size is returned, representing the number of nodes in the graph
- A graph with only one node and edge can be properly returned

All 7/7 tests passing
