def add(*matrices):
    """Add corresponding numbers in given 2-D matrices."""
    matrix_shapes = {
        tuple(len(r) for r in matrix)
        for matrix in matrices
    }
    if len(matrix_shapes) > 1:
        raise ValueError("Given matrices are not the same size.")
    return [
        [sum(values) for values in zip(*rows)]
        for rows in zip(*matrices)
    ]


matrix1 = [[1, -2, 3], [-4, 5, -6], [7, -8, 9]]
matrix2 = [[1, 1, 0], [1, -2, 3], [-2, 2, -2]]
print(add(matrix1, matrix2))
