from lib.input import inputFile, inputMap, inputNode, inputPoint
from lib.output import plot, map, result
from lib.ucs import ucs
from lib.astar import heuristic, haversine, astar
from timeit import timeit

# Read the input file
name, graph = inputFile()

# Plot the graph
path = []
plot(graph, name, path)

# Get the start and end node
start, end = inputNode(name)

# Calculate the shortest path using UCS
ucs_iteration, ucs_cost, ucs_path = ucs(graph, start, end, name)
ucs_time = timeit(lambda: ucs(graph, start, end, name), number=1) * 1000
result("UCS", name, start, end, ucs_iteration, ucs_cost, ucs_path, ucs_time)
plot(graph, name, ucs_path)

# Calculate the shortest path using A*
hfunc = heuristic(graph, end, name)
astar_iteration, astar_cost, astar_path = astar(graph, start, end, name, hfunc)
astar_time = timeit(lambda: astar(graph, start, end, name, hfunc), number=1) * 1000
result("A*", name, start, end, astar_iteration, astar_cost, astar_path, astar_time)
plot(graph, name, astar_path)
