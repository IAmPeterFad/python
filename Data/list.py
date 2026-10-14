# Create Lists
empty = []
letters = ["a", "b", "c", "d", "e", "f"]
numbers = [1, 2, 3]
mixed = [1, "a", True, None]

# print(type(empty))
# print(isinstance(empty, list))
# print(letters)
# print(mixed)

empty = list()
letters = list("Python")
numbers = list(range(1,5))


# Matrix
matrix = [
    ["a", "b", "c"], 
    ["d", "e", "f"]
]

mixed_matrix = [
    ["a", 4, "c"],
    [1, 2],
    [True]
]

# print(matrix)
# print(type(matrix))
# print(mixed_matrix)

# Access and Read
lst = ["a", "b", "c", "d"]

print(lst[-1])

matrix = [
    ["a", "b", "c"],    # Row 1
    ["d", "e", "f"],    # Row 2
    ["g", "h", "i"]     # Row 3
]

print(matrix[0][-1])
print(matrix[1])

# Slicing
print(lst[:2])
print(lst[:])
print(matrix[:2])
print(matrix[0][1:])

# How to unpack data
person = ["Maria", 29, "Data Engineer", "Spain"]
# name = person[0]
# age = person[1]
# role = person[2]
# city = person[3]

name, age, role, country = person
name, *details, country = person
name, *details = person
name, _, role, _ = person
name, *_, country = person

print(name)
print(details)
print(country)
print(*_)

