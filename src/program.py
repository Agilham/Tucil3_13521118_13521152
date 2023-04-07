from ucs import ucs
from astar import astar
from json import loads

def program():
    # Open the text file and read its contents
    name = ["A", "Z", "T", "O", "L", "M" , "S", "D", "R", "F", "C", "P", "B"]
    graph = [[0, 75, 118, 0, 0, 0, 140, 0, 0, 0, 0, 0, 0],
            [75, 0, 0, 71, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [118, 0, 0, 0, 111, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 71, 0, 0, 0, 0, 151, 0, 0, 0, 0, 0, 0],
            [0, 0, 111, 0, 0, 70, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 70, 0, 0, 75, 0, 0, 0, 0, 0],
            [140, 0, 0, 151, 0, 0, 0, 0, 80, 99, 0, 0, 0],
            [0, 0, 0, 0, 0, 75, 0, 0, 120, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 80, 120, 0, 0, 146, 97, 0],
            [0, 0, 0, 0, 0, 0, 99, 0, 0, 0, 0, 0, 211],
            [0, 0, 0, 0, 0, 0, 0, 146, 0, 0, 0, 138, 0],
            [0, 0, 0, 0, 0, 0, 0, 97, 0, 0, 138, 0, 101],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 211, 0, 101, 0]]

    print("Using UCS:")
    iteration, cost, path = ucs(graph, 0, 5, name)
    print(f"\nfinal iteration: {iteration}")
    print(f"final state: cost={cost}, path={path}")

    print("\nUsing A*:")
    iteration, cost, path = astar(graph, 0, 5, name)
    print(f"\nfinal iteration: {iteration}")
    print(f"final state: cost = {cost}, path = {path}")
