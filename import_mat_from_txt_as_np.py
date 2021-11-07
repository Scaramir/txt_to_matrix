import numpy as np


# Option 1:
def matrix_loader(file_name):
    """
    Loads a matrix from a text file.
    """
    with open(file_name, 'r') as f:
        lines = f.readlines()
    lines = [line.strip() for line in lines]
    lines = [line.split(' ') for line in lines]
    lines = [[x for x in line] for line in lines]
    return lines

# Option 2:
def matrix_loader_cheaty(file_name):
    """
    Loads a matrix from a text file as np.
    """
    matrix = np.loadtxt(file_name, delimiter=' ', dtype=np.chararray)
    return matrix


print(matrix_loader('txt.txt'))
print(matrix_loader_cheaty('txt.txt'))
