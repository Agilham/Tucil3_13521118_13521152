from heapq import heappush, heappop
from lib.prioitem import PrioritizedItem

# Calculate the shortest path using UCS
def ucs(graph, start, dest, name):
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
            for neighbor in range(len(graph[node])):
                if graph[node][neighbor] != 0 and neighbor not in visited:
                    # Calculate the actual cost f(n) = g(n)
                    actual_cost = cost + graph[node][neighbor]
                    heappush(queue, PrioritizedItem(actual_cost, neighbor, path))
    # if no path is found, return the iteration count, infinity, and empty path
    return (iteration, float("inf"), [])
