import os
import numpy as np
from scipy.linalg import issymmetric

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
                # check if the matrix is symmetric
                copy = np.array(matrix)
                if not issymmetric(copy):
                    raise ValueError("The adjacency matrix is not symmetric.")
                # if the matrix is valid, return the name and matrix
                return name, matrix
        except (FileNotFoundError, ValueError) as e:
            print(f"Error: {e}")
            continue

# function to get input node from the user
def inputRequest(name: list):
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
