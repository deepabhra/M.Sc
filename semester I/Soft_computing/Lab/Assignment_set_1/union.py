"""
Name: Abhradeep Guin
Class: M.Sc. 1st Year
Assignment 1: Fuzzy Sets and Relations
Question: Union of two Fuzzy Sets
"""

def fuzzy_union(setA, setB):
    union_set = {}
    all_elements = set(setA.keys()) | set(setB.keys())
    for element in all_elements:
        a_val = setA.get(element, 0)
        b_val = setB.get(element, 0)
        union_set[element] = max(a_val, b_val) #Formula: μA∪B​(x)=max{μA​(x),μB​(x)}
    return union_set


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

union = fuzzy_union(setA, setB)

print("\nFuzzy setA: ", setA)
print("Fuzzy setB: ", setB)
print("Union (A U B): ", union)