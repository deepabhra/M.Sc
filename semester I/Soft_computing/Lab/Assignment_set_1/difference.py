"""
Name       : Abhradeep Guin
Class      : M.Sc. 1st Year
Assignment 1: Fuzzy Sets and Relations
Question   : Difference of two Fuzzy Sets
"""

def fuzzy_difference(setA, setB):
    difference_set = {}
    all_elements = set(setA.keys()) | set(setB.keys())
    for element in all_elements:
        a_val = setA.get(element, 0)
        b_val = setB.get(element, 0)
        difference_set[element] = round(min(a_val, 1 - b_val), 4) #round to 4 decimal places to avoid messy values.
    return difference_set


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
setB = input_fuzzy_set("B", n)

difference = fuzzy_difference(setA, setB)

print("\nFuzzy setA: ", setA)
print("Fuzzy setB: ", setB)
print("Difference (A - B): ", difference)