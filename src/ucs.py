from heapq import heappush, heappop
from dataclasses import dataclass, field
from typing import Any

@dataclass(order=True)
class PrioritizedItem:
    cost: int
    node: Any=field(compare=False)
    path: Any=field(compare=False)

def ucs(graph, start, dest, name):
    iteration = 0
    visited = set()
    queue = [PrioritizedItem(0, start, [])]
    while queue:
        iteration += 1
        item = heappop(queue)
        cost = item.cost
        node = item.node
        path = item.path
        print(f"current iteration: {iteration}")
        print(f"current state: cost = {cost}, node = {name[node]}, path = {path}")
        if node not in visited:
            visited.add(node)
            path = path + [name[node]]
            if node == dest:
                return (iteration, cost, path)
            for neighbor in range(len(graph[node])):
                if graph[node][neighbor] != 0 and neighbor not in visited:
                    actual_cost = cost + graph[node][neighbor]
                    heappush(queue, PrioritizedItem(actual_cost, neighbor, path))
    return float("inf"), []