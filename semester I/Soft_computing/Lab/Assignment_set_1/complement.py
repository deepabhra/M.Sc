"""
Name: Abhradeep Guin
Class: M.Sc. 1st Year
Assignment 1: Fuzzy Sets and Relations
Question: Complement of a Fuzzy Set
"""

def fuzzy_complement(setA):
    complement_set = {}
    for element in setA: #Formula: μA​(x)=1−μA​(x)
        complement_set[element] = round(1 - setA[element], 4) #round to 4 decimal places to avoid messy values.
    return complement_set


# To avoid invalid input, it keeps asking until the user enters a value between 0 and 1 (inclusive).

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


def input_fuzzy_set(set_name, n):
    fuzzy_set = {}
    print(f"\nEnter Values of Fuzzy set {set_name}: ")
    for i in range(n):
        element = input(f"Enter element {i+1}: ")
        membership = get_valid_membership(
            f"Enter the membership value for {element} in Set {set_name}: "
        )
        fuzzy_set[element] = membership
    return fuzzy_set



n = int(input("Enter number of elements: "))

setA = input_fuzzy_set("A", n)

complement = fuzzy_complement(setA)

print("\nFuzzy setA: ", setA)
print("Complement (A'): ", complement)