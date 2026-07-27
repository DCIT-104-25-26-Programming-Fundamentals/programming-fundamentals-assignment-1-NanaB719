# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 4
# Topic: Multi-dimensional Arrays (2D Lists), Nested Loops, and Functions
# =============================================================================
#
# TASK: Matrix Operations
#
# Write a Python program that performs three operations on matrices (2D lists),
# each implemented in its own function.
#
# -----------------------------------------------------------------------------
# PART A — Transpose a Matrix
# -----------------------------------------------------------------------------
# - Read an M x N matrix from the user.
# - Compute and display its transpose (rows become columns, columns become rows).
#
# Example (2 x 3 input):
#
#   Original Matrix:      Transposed Matrix:
#   1  2  3               1  4
#   4  5  6               2  5
#                         3  6
#
# -----------------------------------------------------------------------------
# PART B — Add Two Matrices
# -----------------------------------------------------------------------------
# - Read two matrices of exactly the same size (M x N).
# - Compute their element-wise sum and display the result.
#   (Each position in the result = the sum of the values at that position
#    in both matrices.)
#
# -----------------------------------------------------------------------------
# PART C — Multiply Two Matrices
# -----------------------------------------------------------------------------
# - Read matrix A of size M x N and matrix B of size N x P.
#   (The number of COLUMNS in A must equal the number of ROWS in B.)
# - Compute and display the matrix product A × B (result is M x P).
#
# -----------------------------------------------------------------------------
# EXPECTED INPUT FORMAT
# -----------------------------------------------------------------------------
# When entering a row, the user types all values on one line separated by spaces:
#
#   Enter number of rows: 2
#   Enter number of columns: 3
#   Enter row 1: 1 2 3
#   Enter row 2: 4 5 6
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Use nested loops for all operations (no NumPy or other libraries).
# - Each operation must be in its own function (see scaffold below).
# - Display each matrix in a neat, aligned grid format.
# - Tip: Complete Part A first, then Parts B and C.
#

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================

def input_matrix(rows, cols, name="Matrix"):
    matrix = []
    print(f"\nEnter values for {name} ({rows}x{cols}):")
    for i in range(rows):
        row_str = input(f"Enter row {i + 1}: ")
        row = [float(x) for x in row_str.split()]
        matrix.append(row)
    return matrix


def print_matrix(matrix):
    for row in matrix:
        for val in row:
            print(f"{val:6.1f}", end=" ")
        print()


def transpose_matrix(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    result = [[0 for _ in range(rows)] for _ in range(cols)]

    for r in range(rows):
        for c in range(cols):
            result[c][r] = matrix[r][c]

    return result


def add_matrices(mat_a, mat_b):
    rows = len(mat_a)
    cols = len(mat_a[0])
    result = [[0 for _ in range(cols)] for _ in range(rows)]

    for r in range(rows):
        for c in range(cols):
            result[r][c] = mat_a[r][c] + mat_b[r][c]

    return result


def multiply_matrices(mat_a, mat_b):
    rows_a = len(mat_a)
    cols_a = len(mat_a[0])
    cols_b = len(mat_b[0])

    result = [[0 for _ in range(cols_b)] for _ in range(rows_a)]

    for i in range(rows_a):
        for j in range(cols_b):
            for k in range(cols_a):
                result[i][j] += mat_a[i][k] * mat_b[k][j]

    return result


print("--- PART A: Transpose Matrix ---")
r_a = int(input("Enter number of rows: "))
c_a = int(input("Enter number of columns: "))
mat_a = input_matrix(r_a, c_a, "Matrix A")

print("\nOriginal Matrix:")
print_matrix(mat_a)

print("\nTransposed Matrix:")
transposed = transpose_matrix(mat_a)
print_matrix(transposed)

print("\n--- PART B: Add Two Matrices ---")
print(f"Entering Matrix B of same size ({r_a}x{c_a})...")
mat_b = input_matrix(r_a, c_a, "Matrix B")

print("\nMatrix A + Matrix B:")
added = add_matrices(mat_a, mat_b)
print_matrix(added)

print("\n--- PART C: Multiply Two Matrices ---")
print(f"For A x B, Matrix C rows MUST equal Matrix A columns ({c_a}).")
cols_c = int(input("Enter number of columns for Matrix C: "))
mat_c = input_matrix(c_a, cols_c, "Matrix C")

print("\nMatrix A x Matrix C:")
multiplied = multiply_matrices(mat_a, mat_c)
print_matrix(multiplied)