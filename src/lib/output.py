import networkx as nx
import folium
import osmnx as ox
import os
import matplotlib.pyplot as plt

# Plot the graph and highlight the shortest path
def plot(graph, name, path):
    # Define the vertex labels
    labels = {k: v for k, v in enumerate(name)}

    # Convert the adjacency matrix to a weighted graph
    G = nx.Graph()
    for i in range(len(graph)):
        for j in range(i+1, len(graph[i])):
            if graph[i][j] != 0:
                G.add_edge(labels[i], labels[j], weight=graph[i][j])

    # Plot the weighted graph with the shortest path highlighted
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, font_weight='bold')
    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_weight='bold')
    edge_colors = ['b' if (path[i], path[i+1]) in nx.edges(G) else 'k' for i in range(len(path)-1)]
    nx.draw_networkx_edges(G, pos, edgelist=[(path[i], path[i+1]) for i in range(len(path)-1)], edge_color='r', width=4)
    nx.draw_networkx_edges(G, pos, edge_color=edge_colors)
    plt.show()

# Plot the graph on a map and highlight the shortest path
def map(graph, center, route, algorithm):
    filename = f'route-{algorithm}.html'
    filepath = os.path.join('..\\Tucil3_13521118_13521152\\test', filename)
    m = folium.Map(location=[center[0], center[1]], zoom_start=12)
    ox.plot_route_folium(graph, route, route_map=m, line_color='blue', line_weight=5)
    # Save the map to an HTML file
    m.save(filepath)

# Print the result of the algorithm
def result(function, name, start, end, iteration, cost, path, time):
    print(f"-----------------------------")
    print(f"Algorithm: {function}")
    print(f"Start node: {name[start]}")
    print(f"End node: {name[end]}")
    print(f"Shortest path: {path}")
    print(f"Shortest distance: {cost}")
    print(f"Iteration count: {iteration}")
    print(f"Elapsed time: {time} miliseconds")
