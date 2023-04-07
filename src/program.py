from ucs import ucs
from astar import astar, heuristic
import timeit

def program():
    # Open the text file and read its contents
    name = ["A", "B", "C", "D", "E", "F"]
    graph = [[0, 2, 4, 0, 5, 0],
             [2, 0, 0, 0, 1, 0],
             [4, 0, 0, 3, 0, 0],
             [0, 0, 3, 0, 3, 1],
             [5, 1, 0, 3, 0, 2],
             [0, 0, 0, 1, 2, 0]]

    print("Using UCS:")
    iteration, cost, path = ucs(graph, 0, 5, name)
    ucs_time = timeit.timeit(lambda: ucs(graph, 0, 1, name), number=1000) * 1000
    print(f"final iteration: {iteration}")
    print(f"final state: cost={cost}, path={path}")
    print(f"elapsed time: {ucs_time} miliseconds")
    
    print("\nUsing A*:")
    h = heuristic(graph, 5, name)
    iteration, cost, path = astar(graph, 0, 5, name, h)
    astar_time = timeit.timeit(lambda: astar(graph, 0, 5, name, h), number=1000) * 1000
    print(f"final iteration: {iteration}")
    print(f"final state: cost = {cost}, path = {path}")
    print(f"elapsed time: {astar_time} miliseconds")
