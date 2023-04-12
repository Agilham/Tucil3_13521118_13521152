from lib.input import inputMethod, inputFile, inputMap, inputNode, inputPoint
from lib.output import plot, map, result
from lib.ucs import ucs
from lib.astar import heuristic, haversine, astar
from timeit import timeit

# Get the input method
isFile = inputMethod()

if (isFile):
    # Read the input file
    name, adj_matrix = inputFile()
    # Plot the graph
    path = []
    plot(adj_matrix, name, path)
    # Get the start and end node
    start, end = inputNode(name)
else:
    # Read the map coordinates
    center, radius, graph, name, adj_matrix, bbox = inputMap()
    # Get the start and end point
    start, end = inputPoint(graph, bbox)

# Calculate the shortest path using UCS
ucs_iteration, ucs_cost, ucs_path = ucs(adj_matrix, start, end, name)
ucs_time = timeit(lambda: ucs(adj_matrix, start, end, name), number=1) * 1000
result("UCS", name, start, end, ucs_iteration, ucs_cost, ucs_path, ucs_time)
if (len(ucs_path) == 0):
    print("No path found")
else:
    if (isFile):
        plot(adj_matrix, name, ucs_path)
    else:
        map(graph, center, ucs_path, "UCS")

# Calculate the shortest path using A*
if (isFile):
    hfunc = heuristic(adj_matrix, end, name)
else:
    hfunc = haversine(adj_matrix, graph, end)
astar_iteration, astar_cost, astar_path = astar(adj_matrix, start, end, name, hfunc)
astar_time = timeit(lambda: astar(adj_matrix, start, end, name, hfunc), number=1) * 1000
result("A*", name, start, end, astar_iteration, astar_cost, astar_path, astar_time)
if (len(astar_path) == 0):
    print("No path found")
else:
    if (isFile):
        plot(adj_matrix, name, astar_path)
    else:
        map(graph, center, astar_path, "A-star")
