"""
Name: Abhradeep Guin
Class: M.Sc. 1st Year
Assignment 1: Fuzzy Sets and Relations
Question: Max-Min Composition of two Fuzzy Relations
"""

def max_min_composition(R, S, m, n, p):
    T = [[0 for _ in range(p)] for _ in range(m)]
    for i in range(m):
        for j in range(p):
            values = []
            for k in range(n):
                values.append(min(R[i][k], S[k][j])) #Formula: C = A ∘ B, Cᵢⱼ = maxₖ { min(aᵢₖ, bₖⱼ) }
            T[i][j] = round(max(values), 4)
    return T


# Fuzzy relation values must be between 0 and 1 (inclusive).

def get_valid_membership(valid_input):
    while True:
        try:
            value = float(input(valid_input))
        except ValueError:
            print("\nInvalid input! Please enter a number.\n")
            continue
        if 0 <= value <= 1:
            return value
        else:
            print("\nInvalid! Membership value must be between 0 and 1. Try again.\n")


def input_matrix(name, rows, cols):
    matrix = []
    print(f"\nEnter values for relation {name} ({rows} x {cols}):")
    for i in range(rows):
        row = []
        for j in range(cols):
            value = get_valid_membership(f"{name}[{i+1}][{j+1}]: ")
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

# OUTPUT
'''
Enter number of rows in R (elements in X): 2
Enter number of columns in R / rows in S (elements in Y): 3
Enter number of columns in S (elements in Z): 2

Enter values for relation R (2 x 3):
R[1][1]: 0.7
R[1][2]: 0.2
R[1][3]: 0.9
R[2][1]: 0.3
R[2][2]: 0.8
R[2][3]: 0.5

Enter values for relation S (3 x 2):
S[1][1]: 0.6
S[1][2]: 4

Invalid! Membership value must be between 0 and 1. Try again.

S[1][2]: 0.4
S[2][1]: 0.5
S[2][2]: 0.9
S[3][1]: 0.2
S[3][2]: 0.7

Relation R (X x Y):
[0.7, 0.2, 0.9]
[0.3, 0.8, 0.5]

Relation S (Y x Z):
[0.6, 0.4]
[0.5, 0.9]
[0.2, 0.7]

Composition T = R∘S (X x Z) [Max-Min]:
[0.6, 0.7]
[0.5, 0.8]
'''