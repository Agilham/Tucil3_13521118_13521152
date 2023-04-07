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
        if size >= 8:
            print(" ".join(name))
            # Reading the adjacency matrix
            matrix = []
            for i in range(size):
                line = f.readline()
                row = [int(x) for x in line.strip().split()]
                matrix.append(row)
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
inputFile()


    

    