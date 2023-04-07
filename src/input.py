import os

def inputFile():
    # Opening input file
    filename = input("Masukkan nama file input: ")
    filePath = os.path.join('..\\Tucil3_13521118_13521152\\test', filename)
    with open(filePath, 'r') as f:
        # Reading the name of nodes
        line = f.readline()
        name = [str(x) for x in line.strip().split()]
        # Get the number of nodes
        size = len(name)
        # Check if the number of nodes is at least 8
        if size >= 0:
            # Reading the adjacency matrix
            matrix = []
            for i in range(size):
                line = f.readline()
                row = [int(x) for x in line.strip().split()]
                rowLength = len(row)
                if(rowLength != size):
                    print("Matriks ketetanggaan tidak valid")
                    inputFile()
                    break
                for rows in row:
                    if(rows < 0):
                        print("Elemen matriks ketetanggaan tidak valid")
                        inputFile()
                        break
                matrix.append(row)
            print("\nDaftar simpul:")
            print(" ".join(name))
            # Print the adjacency matrix
            print("\nMatriks ketetanggaan:")
            for row in matrix:
                print(row)
            # Return the name of nodes and the adjacency matrix
            return name, matrix
        else:
            # If the number of nodes is less than 8, ask for another file
            print("Silahkan masukkan file dengan setidaknya 8 simpul")
            # Call the function again
            inputFile()

def inputRequest(name : list):
    print("\nDaftar simpul valid:")
    for i in range(len(name)):
        print(f"{i+1}. {name[i]}")
    inputNode = int(input("Masukkan simpul awal: "))
    while (inputNode < 1) or (inputNode > len(name)):
        print("Masukkan simpul awal yang valid")
        inputNode = int(input("Masukkan simpul awal: "))
    startNode = inputNode-1
    
    print("\nDaftar simpul valid:")
    for i in range(len(name)):
        if (i < startNode):
            print(f"{i+1}. {name[i]}")
        elif (i > startNode):
            print(f"{i}. {name[i]}")
    inputNode = int(input("Masukkan simpul tujuan: "))
    while (inputNode < 1) or (inputNode > len(name)-1):
        print("Masukkan simpul tujuan yang valid")
        inputNode = int(input("Masukkan simpul tujuan: "))
    if (inputNode-1 < startNode):
        endNode = inputNode-1
    else:
        endNode = inputNode
    return startNode, endNode

name, matrix = inputFile()
startNode, endNode = inputRequest(name)
print(f"\nSimpul awal: {name[startNode]}")
print(f"Simpul tujuan: {name[endNode]}")