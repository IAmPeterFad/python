numbers = [1, 5, 5, 2, 4]

print("Max:", max(numbers))
print("Min:", min(numbers))
print("Sun:", sum(numbers))
print("Length:", len(numbers))

print("All:", all(numbers))
print("All:", all([1, 0, 2]))
print("All:", all(['a', '', 'c']))

print("Any:", any(numbers))
print("Any:", any([1, 0, 2]))
print("Any:", any(['a', '', 'c']))
print("Any:", any([0, 0, 0, 0]))

print("Count:", numbers.count(5))
print("Index:", numbers.index(5))
print(8 in numbers)
