import numpy as np
SIZE = 4

def forward_gaussian_move(matrix, vector_b):
    for i in range(SIZE-1):
        max_elem = matrix[i][i]
        max_row = i
        for j in range(i+1, SIZE):
            if abs(matrix[j][i]) > abs(max_elem):
                max_elem = matrix[j][i]
                max_row = j
        if max_row != i:
            matrix[i], matrix[max_row] = matrix[max_row], matrix[i]
            vector_b[i], vector_b[max_row] = vector_b[max_row], vector_b[i]
        for j in range(i+1, SIZE):
            coefficient = matrix[j][i] / matrix[i][i]
            for k in range(i, SIZE):
                matrix[j][k] -= coefficient * matrix[i][k]
            vector_b[j] -= coefficient * vector_b[i]

def solve_system(matrix, vector_b):
    solution = np.zeros(SIZE)
    for i in range(SIZE-1, -1, -1):
        _sum = 0
        for j in range(i+1, SIZE):
            _sum += matrix[i][j] * solution[j]
        solution[i] = (vector_b[i] - _sum) / matrix[i][i]
    return solution

def calculate_delta(matrix, vector_b, solution):
    Ax = np.dot(matrix, solution)
    delta = np.linalg.norm(Ax - vector_b)
    return delta

def matrix_vector_product(matrix, vector_b):
    return np.dot(matrix, vector_b)

def vector_sum(vector_a, vector_b):
    return np.add(vector_a, vector_b)

def vector_difference(vector_a, vector_b):
    return np.subtract(vector_a, vector_b)

def vector_norm(vector_a):
    return np.linalg.norm(vector_a)

def main():
    matrix = np.array([
        [7*np.pi, 2, 2, 1],
        [1, 7*np.pi, 1, 3],
        [1, 3, 5*np.pi, 4],
        [4, 4, 3, 8*np.pi]
    ])
    vector_b = np.array([2, 8, 1, 7])
    print("Matrix A and vector b:")
    print(np.column_stack((matrix, vector_b)))
    print("\nUpper triangular A and vector B:")
    forward_gaussian_move(matrix, vector_b)
    print(np.column_stack((matrix, vector_b)))
    print("\nSolution vector:")
    solution = solve_system(matrix, vector_b)
    print(solution)
    delta = calculate_delta(matrix, vector_b, solution)
    print("\nError:", delta)
    product = matrix_vector_product(matrix, vector_b)
    print("\nProduct of matrix and vector:")
    print(product)
    first_vector = np.array([1, 2, 3, 4])
    second_vector = np.array([3, 2, 1, 5])
    _sum = vector_sum(first_vector, second_vector)
    print("\nSum of vectors:")
    print(_sum)
    difference = vector_difference(first_vector, second_vector)
    print("\nDifference of vectors:")
    print(difference)
    norm = vector_norm(first_vector)
    print("\nEuclidean norm of vector A:", norm)

if __name__ == "__main__":
    main()