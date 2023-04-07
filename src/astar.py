from heapq import heappush, heappop
from dataclasses import dataclass, field
from typing import Any
from copy import deepcopy

@dataclass(order=True)
class PrioritizedItem:
    cost: int
    node: Any=field(compare=False)
    path: Any=field(compare=False)

def unweigh(graph):
    copy = deepcopy(graph)
    for i in range(len(graph)):
        for j in range(len(graph)):
            if graph[i][j] != 0:
                copy[i][j] = 1
    return copy

def heuristic(adj_matrix, dest_vertex):
    n = len(adj_matrix)
    distances = [[float('inf') if adj_matrix[i][j] == 0 else adj_matrix[i][j] for j in range(n)] for i in range(n)]
    distances[dest_vertex][dest_vertex] = 0
    
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if distances[i][j] > distances[i][k] + distances[k][j]:
                    distances[i][j] = distances[i][k] + distances[k][j]
    
    return [distances[i][dest_vertex] for i in range(n)]

def astar(graph, start, dest, name):
    unweighted = unweigh(graph)
    h = heuristic(unweighted, dest)
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
            if (node != start):
                cost -= h[node]
            for neighbor in range(len(graph[node])):
                if graph[node][neighbor] != 0 and neighbor not in visited:
                    actual_cost = cost + graph[node][neighbor] + h[neighbor]
                    heappush(queue, PrioritizedItem(actual_cost, neighbor, path))
    return float("inf")
