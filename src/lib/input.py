import os
import osmnx as ox
import networkx as nx

# function to get input file from the user
def inputFile():
    while True:
        # opening input file
        filename = input("Enter the name of the input file :\n")
        filepath = os.path.join('..\\Tucil3_13521118_13521152\\test', filename)
        
        try:
            with open(filepath, 'r') as f:
                # reading the name of nodes
                line = f.readline()
                name = [str(x) for x in line.strip().split(', ')]
                # get the number of nodes
                size = len(name)
                # check if the number of nodes is at least 8
                if size < 8:
                    raise ValueError("Input file must contain at least 8 nodes.")
                
                # reading the adjacency matrix
                matrix = []
                for i in range(size):
                    line = f.readline()
                    row = line.strip().split()
                    # check if row length is valid
                    if len(row) != size:
                        raise ValueError("The adjacency matrix is not rectangular.")
                    # check if all elements are non-negative integers
                    try:
                        row = [int(element) for element in row]
                        if any(element < 0 for element in row):
                            raise ValueError("Elements of the adjacency matrix must be non-negative integers.")
                        matrix.append(row)
                    except ValueError:
                        raise ValueError("File contains non-integer elements.")
                # if the matrix is valid, return the name and matrix
                return name, matrix
        except (FileNotFoundError, ValueError) as e:
            print(f"Error: {e}")
            continue

def inputMap():
    print("Range of valid latitude: -90 to 90")
    lat = float(input('Enter the latitude of the center point: '))
    print("Range of valid longitude: -180 to 180")
    lon = float(input('Enter the longitude of the center point: '))
    center = (lat, lon)
    radius = int(input('Enter the radius of the area (in meters): '))

    graph = ox.graph_from_point(center, dist=radius, network_type='drive')
    graph = nx.relabel.convert_node_labels_to_integers(graph)

    coordinates = []
    node_attributes = graph.nodes.data()
    for node_id, node_data in node_attributes:
        y = round(float(node_data['y']), 5)
        x = round(float(node_data['x']), 5)
        coordinates.append((y, x))

    min_lat = min(coordinates, key=lambda x: x[0])[0]
    min_lon = min(coordinates, key=lambda x: x[1])[1]
    max_lat = max(coordinates, key=lambda x: x[0])[0]
    max_lon = max(coordinates, key=lambda x: x[1])[1]

    south, west, north, east = ox.utils_geo.bbox_from_point((lat, lon), dist=radius, project_utm=False)

    adj_matrix = nx.to_numpy_array(graph, weight='length')
    name = []
    for i in range(len(adj_matrix)):
        name.append(i)

    return adj_matrix, graph, name, min_lat, min_lon, max_lat, max_lon

# function to get input node from the user
def inputNode(name: list):
    print("-----------------------------")
    print("List of valid nodes :")
    for i in range(len(name)):
        print(f"{i+1}. {name[i]}")
    # get the starting node
    while True:
        try:
            inputNode = int(input("Choose the starting node : "))
            if inputNode < 1 or inputNode > len(name):
                print("Enter a valid starting node")
                continue
            startNode = inputNode - 1
            break
        except ValueError:
            print("Enter a valid integer")
    print("-----------------------------")
    print("List of valid nodes :")
    for i in range(len(name)):
        if i < startNode:
            print(f"{i+1}. {name[i]}")
        elif i > startNode:
            print(f"{i}. {name[i]}")
    # get the destination node
    while True:
        try:
            inputNode = int(input("Choose the destination node : "))
            if inputNode < 1 or inputNode > len(name) - 1:
                print("Enter a valid destination node")
                continue
            if inputNode - 1 < startNode:
                endNode = inputNode - 1
            else:
                endNode = inputNode
            break
        except ValueError:
            print("Enter a valid integer")
    # if the input is valid, return the starting and destination node
    return startNode, endNode

def inputPoint(graph):
    lat_0 = float(input('Enter the latitude of the start point: '))
    lon_0 = float(input('Enter the longitude of the start point: '))
    lat_1 = float(input('Enter the latitude of the destination point: '))
    lon_1 = float(input('Enter the longitude of the destination point: '))
    origin_node = ox.nearest_nodes(graph, lon_0, lat_0)
    destination_node = ox.nearest_nodes(graph, lon_1, lat_1)
