from ucs import ucs
from astar import astar, heuristic
from input import inputFile, inputRequest
import timeit

def program():
    # Read the input file
    name, graph = inputFile()
    # Get the start and end node
    start, end = inputRequest(name)

    print("\nUsing UCS:")
    print(f"start node: {name[start]}, end node: {name[end]}")
    iteration, cost, path = ucs(graph, start, end, name)
    ucs_time = timeit.timeit(lambda: ucs(graph, start, end, name), number=1) * 1000
    print(f"iteration count: {iteration}")
    print(f"cost = {cost}, path = {path}")
    print(f"elapsed time: {ucs_time} miliseconds")
    
    print("\nUsing A*:")
    print(f"start node: {name[start]}, end node: {name[end]}")
    h = heuristic(graph, end, name)
    iteration, cost, path = astar(graph, start, end, name, h)
    astar_time = timeit.timeit(lambda: astar(graph, start, end, name, h), number=1) * 1000
    print(f"iteration count: {iteration}")
    print(f"cost: {cost}, path: {path}")
    print(f"elapsed time: {astar_time} miliseconds")
