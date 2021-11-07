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
    Loads a matrix from a text file to np.
    """
    matrix = np.loadtxt(file_name, delimiter=' ', dtype=np.chararray)

    return matrix

matrix_a = matrix_loader('txt.txt')
print(matrix_a)
matrix_b = matrix_loader_cheaty('txt.txt')
print(matrix_b)


# Single-linkage Clustering 
# (Beware, not mine! This is just an example solution based on wiki git and random 3am motivation! At least I think so...; will check it tomorrow!) 
def UPGMA(matrix):
    """
    UPGMA clustering algorithm.
    """
    # Initialize the distance matrix.
    matrix = np.array(matrix)
    distance_matrix = np.zeros((len(matrix), len(matrix)))
    distance_matrix[:] = np.inf

    # Set the diagonal of the distance matrix to 0.
    for i in range(len(matrix)):
        distance_matrix[i, i] = 0

    # Iteratively update the distance matrix.
    while len(matrix) > 2:
        # Find the minimum distance in the distance matrix.
        min_dist = np.min(distance_matrix)
        min_dist_i = np.where(distance_matrix == min_dist)[0][0]
        min_dist_j = np.where(distance_matrix == min_dist)[1][0]

        # Merge the two closest clusters.
        matrix = np.vstack((matrix[min_dist_i], matrix[min_dist_j]))
        matrix = np.delete(matrix, [min_dist_j, min_dist_i], axis=0)

        # Update the distance matrix.
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                if i != j:
                    distance_matrix[i, j] = np.min(
                        [distance_matrix[i, j],
                         distance_matrix[i, min_dist_i] +
                         distance_matrix[min_dist_j, j]])

    return matrix
