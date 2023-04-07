import os

def inputFile():
    while True:
        # opening input file
        filename = input("Masukkan nama file input: ")
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
                    raise ValueError("File tidak memiliki setidaknya 8 simpul.")
                
                # reading the adjacency matrix
                matrix = []
                for i in range(size):
                    line = f.readline()
                    row = [int(x) for x in line.strip().split()]
                    # check if row length is valid
                    if len(row) != size:
                        raise ValueError("Matriks ketetanggaan tidak valid.")
                    # check if all elements are non-negative
                    if any(element < 0 for element in row):
                        raise ValueError("Elemen matriks ketetanggaan tidak valid.")
                    matrix.append(row)
                # if everything is valid, return the name and matrix
                return name, matrix

        except (FileNotFoundError, ValueError) as e:
            print(f"Error: {e}")
            continue

        

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