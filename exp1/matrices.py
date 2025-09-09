def add_matrices(matrix1, matrix2):
    result = []
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix1[0])):
            row.append(matrix1[i][j] + matrix2[i][j])
        result.append(row)
    return result

def input_matrix(rows, cols, matrix_num):
    print(f"Enter values for matrix {matrix_num}:")
    matrix = []
    for i in range(rows):
        while True:
            row_input = input(f"Row {i + 1} (enter {cols} numbers separated by spaces): ")
            row = row_input.strip().split()
            if len(row) != cols:
                print(f"Please enter exactly {cols} numbers.")
                continue
            try:
                row = [int(x) for x in row]
                break
            except ValueError:
                print("Please enter valid integers.")
        matrix.append(row)
    return matrix

rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of columns: "))

matrix1 = input_matrix(rows, cols, 1)
matrix2 = input_matrix(rows, cols, 2)

sum_matrix = add_matrices(matrix1, matrix2)

print("Result of matrix addition:")
for row in sum_matrix:
    print(row)
