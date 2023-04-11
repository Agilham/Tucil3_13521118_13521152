from heapq import heappush, heappop
from lib.prioitem import PrioritizedItem
from lib.ucs import ucs
from math import radians, cos, sqrt

EARTH_RADIUS = 6371000

# Calculate the heuristic value for each node using UCS
def heuristic(adj_matrix, dest, name):
    h = [0] * len(adj_matrix)
    for node in range(len(adj_matrix)):
        iteration, cost, path = ucs(adj_matrix, node, dest, name)
        h[node] = cost
    return h

# Calculate the heuristic value for each node using Haversine
def haversine(adj_matrix, graph, destination_node):
    h = [0] * len(adj_matrix)
    dest_lat = radians(graph.nodes[destination_node]['y'])
    dest_lon = radians(graph.nodes[destination_node]['x'])
    for u in graph.nodes():
        lat1 = radians(graph.nodes[u]['y'])
        lon1 = radians(graph.nodes[u]['x'])
        x = (lon1 - dest_lon) * cos(0.5 * (lat1 + dest_lat))
        y = lat1 - dest_lat
        euclidean_distance = EARTH_RADIUS * sqrt(x * x + y * y)
        h[u] = euclidean_distance
    return h

# Calculate the shortest path using A*
def astar(adj_matrix, start, dest, name, heuristic):
    iteration = 0
    visited = set()
    queue = [PrioritizedItem(0, start, [])]
    while queue:
        iteration += 1
        item = heappop(queue)
        cost, node, path = item.cost, item.node, item.path
        if node not in visited:
            visited.add(node)
            path = path + [name[node]]
            if node == dest:
                # if shortest path is found, return the iteration count, cost, and path
                return (iteration, cost, path)
            if (node != start):
                cost -= heuristic[node]
            for neighbor in range(len(adj_matrix[node])):
                if adj_matrix[node][neighbor] != 0 and neighbor not in visited:
                    # Calculate the actual cost f(n) = g(n) + h(n)
                    actual_cost = cost + adj_matrix[node][neighbor] + heuristic[neighbor]
                    heappush(queue, PrioritizedItem(actual_cost, neighbor, path))
    # if no path is found, return the iteration count, infinity, and empty path
    return (iteration, float("inf"), [])
