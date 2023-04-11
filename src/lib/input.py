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
    # get the center point  the area
    print("Range of valid latitude: -90 to 90")
    lat = float(input('Enter the latitude of the center point: '))
    print("Range of valid longitude: -180 to 180")
    lon = float(input('Enter the longitude of the center point: '))
    center = (lat, lon)

    # get the radius of the area
    print("Range of valid radius: 500 to 5000")
    radius = int(input('Enter the radius of the area (in meters): '))

    # make a graph from the center point and radius
    graph = ox.graph_from_point(center, dist=radius, network_type='drive')
    graph = nx.relabel.convert_node_labels_to_integers(graph)

    # get the name of the nodes
    name = []
    for node in graph.nodes():
        name.append(node)

    # convert graph to adjacency matrix
    adj_matrix = nx.to_numpy_array(graph, weight='length')
    # get the bounding box of the graph
    bbox = ox.utils_geo.bbox_from_point(center, dist=radius, project_utm=False)

    # if all inputs are valid, return the center point, radius, graph, name, adjacency matrix, and bounding box
    return center, radius, graph, name, adj_matrix, bbox

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

def inputPoint(graph, bbox):
    print("-----------------------------")
    # get the starting point
    print("Valid latitude range:", bbox[1], "to", bbox[0])
    startLat = float(input('Enter the latitude of the start point: '))
    print("Valid longitude range:", bbox[3], "to", bbox[2])
    startLon = float(input('Enter the longitude of the start point: '))

    print("-----------------------------")
    # get the destination point
    print("Valid latitude range:", bbox[1], "to", bbox[0], "except", startLat)
    endLat = float(input('Enter the latitude of the destination point: '))
    print("Valid longitude range:", bbox[3], "to", bbox[2], "except", startLon)
    endLon = float(input('Enter the longitude of the destination point: '))

    # define the starting and destination node
    startNode = ox.nearest_nodes(graph, startLon, startLat)
    endNode = ox.nearest_nodes(graph, endLon, endLat)

    return startNode, endNode
