import os
import osmnx as ox
import networkx as nx
import numbers

# function to get the input method from the user
def inputMethod():
    # get the input method
    print("Valid Input Method:")
    print("1. File Input")
    print("2. Map Coordinates Input")
    while True:
        choice = input("Choose the input method: ")
        if choice == "1":
            isFile = True
            break
        elif choice == "2":
            isFile = False
            break
        else:
            print("Enter a valid input method")
    # if the input is valid, return the input method
    return isFile

# function to get input file from the user
def inputFile():
    print("-----------------------------")
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
    print("-----------------------------")
    valid = False
    while not valid:
        # get the center point of the area
        print("Valid latitude range: -90 to 90 (in degreess)")
        while True:
            try:
                lat = float(input('Enter the latitude of the center point: '))
                if lat < -90 or lat > 90:
                    print("Enter a valid latitude")
                    continue
                break
            except ValueError:
                print("Enter a number (in degrees) for latitude")
        print("Valid longitude range: -180 to 180 (in degrees)")
        while True:
            try:
                lon = float(input('Enter the longitude of the center point: '))
                if lon < -180 or lon > 180:
                    print("Enter a valid longitude")
                    continue
                break
            except ValueError:
                print("Enter a number (in degrees) for longitude")
        center = (lat, lon)

        # get the radius of the area
        print("Valid radius range: 500 to 5000 (in meters)")
        while True:
            try:
                radius = int(input('Enter the radius of the area: '))
                if radius < 500 or radius > 5000:
                    print("Enter a valid radius")
                    continue
                break
            except ValueError:
                print("Enter a number for radius")

        try:
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
            valid = True
            return center, radius, graph, name, adj_matrix, bbox
        # if there are no nodes in the graph, print the error and ask for new center point and radius
        except ValueError as e:
            print(f"Error: {e}")
            print("Enter a new center point and radius")

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
            print("Enter the number (integer) of the node")
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
            print("Enter the number (integer) of the node")
    # if the input is valid, return the starting and destination node
    return startNode, endNode

def inputPoint(graph, bbox):
    print("-----------------------------")
    # get the starting point
    print("Valid latitude range:", bbox[1], "to", bbox[0], "(in degrees)")
    while True:
        try:
            startLat = float(input('Enter the latitude of the start point: '))
            if not isinstance(startLat, numbers.Number):
                raise ValueError()
            if startLat < bbox[1] or startLat > bbox[0]:
                print("Enter a valid start point latitude")
            else:
                break
        except ValueError:
            print("Enter a number (in degrees) for latitude")
    print("Valid longitude range:", bbox[3], "to", bbox[2], "(in degrees)")
    while True:
        try:
            startLon = float(input('Enter the longitude of the start point: '))
            if not isinstance(startLon, numbers.Number):
                raise ValueError()
            if startLon < bbox[3] or startLon > bbox[2]:
                print("Enter a valid start point longitude")
            else:
                break
        except ValueError:
            print("Enter a number (in degrees) for longitude")

    print("-----------------------------")
    # get the destination point
    print("Valid latitude range:", bbox[1], "to", bbox[0], "(in degrees)")
    while True:
        try:
            endLat = float(input('Enter the latitude of the destination point: '))
            if not isinstance(endLat, numbers.Number):
                raise ValueError()
            if endLat < bbox[1] or endLat > bbox[0]:
                print("Enter a valid destination point latitude")
            else:
                break
        except ValueError:
            print("Enter a number (in degrees) for latitude")
    print("Valid longitude range:", bbox[3], "to", bbox[2], "(in degrees)")
    while True:
        try:
            endLon = float(input('Enter the longitude of the destination point: '))
            if not isinstance(endLon, numbers.Number):
                raise ValueError()
            if endLon < bbox[3] or endLon > bbox[2]:
                print("Enter a valid destination point longitude")
            else:
                break
        except ValueError:
            print("Enter a number (in degrees) for longitude")

    # define the starting and destination node
    startNode = ox.nearest_nodes(graph, startLon, startLat)
    endNode = ox.nearest_nodes(graph, endLon, endLat)

    # if the input is valid, return the starting and destination node
    return startNode, endNode
