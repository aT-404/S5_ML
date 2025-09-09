rows1 = int(input("\nMatrix 1\nEnter the number of rows: "))
cols1 = int(input("Enter the number of columns: "))
rows2 = int(input("Matrix 2\nEnter the number of rows: "))
cols2 = int(input("Enter the number of columns: "))

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
            row = [int(x) for x in row]
            break

        matrix.append(row)
    return matrix

if cols1 != rows2:
    print("\nCant multiply the matrix!!!\n")
else:
    matrix1 = input_matrix(rows1, cols1, 1)
    matrix2 = input_matrix(rows2, cols2, 2)
    result = [[sum (matrix1[i][k]* matrix2[k][j] for k in range(cols1))for j in range (cols2)]for i in range (rows1)]

    print ("\nResultant matrix is:")
    for row in result:
        print(row)