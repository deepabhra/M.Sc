"""
Name       : Abhradeep Guin
Class      : M.Sc. 1st Year
Assignment 1: Fuzzy Sets and Relations
Question   : Max-Min Composition of two Crisp Relations
"""

def max_min_composition(R, S, m, n, p):
    T = [[0 for _ in range(p)] for _ in range(m)]
    for i in range(m):
        for j in range(p):
            values = []
            for k in range(n):
                values.append(min(R[i][k], S[k][j]))
            T[i][j] = max(values)
    return T


# Crisp relation values must be exactly 0 or 1 (not fuzzy degrees).

def get_crisp_value(valid_input):
    while True:
        try:
            value = int(input(valid_input))
        except ValueError:
            print("\nInvalid input! Please enter 0 or 1.\n")
            continue
        if value in (0, 1):
            return value
        else:
            print("\nInvalid! Crisp relation value must be 0 or 1. Try again.\n")


def input_matrix(name, rows, cols):
    matrix = []
    print(f"\nEnter values for relation {name} ({rows} x {cols}):")
    for i in range(rows):
        row = []
        for j in range(cols):
            value = get_crisp_value(f"{name}[{i+1}][{j+1}]: ")
            row.append(value)
        matrix.append(row)
    return matrix


def print_matrix(name, matrix):
    print(f"\n{name}:")
    for row in matrix:
        print(row)



m = int(input("Enter number of rows in R (elements in X): "))
n = int(input("Enter number of columns in R / rows in S (elements in Y): "))
p = int(input("Enter number of columns in S (elements in Z): "))

R = input_matrix("R", m, n)
S = input_matrix("S", n, p)

T = max_min_composition(R, S, m, n, p)

print_matrix("Relation R (X x Y)", R)
print_matrix("Relation S (Y x Z)", S)
print_matrix("Composition T = R∘S (X x Z) [Max-Min]", T)