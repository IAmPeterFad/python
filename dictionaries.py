# Dictionaries
band = {
    "Vocals" : "Plants",
    "guiter" : "Page"
}

band2 = dict(Vocals = "Plants", guiter = "Page")

print(band)
print(band2)
print(type(band))
print(len(band2))

# Access items
print(band["Vocals"])
print(band.get("guiter"))

# List all keys
print(band.keys())

# List all values
print(band.values())

# List of key/value pairs as tuples
print(band.items())

# Verify if a key exist
print("Vocals" in band)
print("Cowbell" in band)

# Change value in dictionaries
band["Vocals"] = "Coverdale"
band.update({"Bass": 'JPJ'})
print(band)

# Rmove items
print(band.pop("Bass"))
print(band)

band["drums"] = "Bonham"
print(band)

print(band.popitem())  # Tuple
print(band)

# Delete and clear an items
band.update({"drums": "Bonham"})
print(band)
del band["drums"]
print(band)

band2.clear()
print(band2)

del band2

# Copy dictionaries
# band2 = band # create a reference
# print("Bad copy!")
# print(band)
# print(band2)

# band2["grace"] = "Peter"
# print(band)

band2 = band.copy()
band2["drums"] = "Peter"
print("Good copy!")
print(band)
print(band2)

# Nested dictionaries
member1 = {
    "name": "Plant",
    "instrument": "vocals"
}
member2 = {
    "name": "Page",
    "instrument": "guitar"
}

band = {
    "member1": member1,
    "member2": member2
}

print(band)
print(band["member1"]["name"])

# Sets
nums = { 1, 2, 3, 4}
nums2 = set((1,2,3,4))

print(nums)
print(nums2)
print(type(nums))
print(len(nums))

# No duplicate allowed
nums = {1, 2, 2, 3}
print(nums)

# True is a dupe of 1, False is a dupe of zero
nums = {1, True, 2, 3, False, 4, 0}
print(nums)

# Check if value is in a set
print(2 in nums)

# But you cannot refer to an element in a set with index or key

# Add a new element to a set
nums.add(8)
print(nums)

# Add element from one set togetheir
morenums = {5, 6, 7}
nums.update(morenums)
print(nums)

# You can use update with lists, tuple and dictionaries too.

# Merge two sets to create a new set
one = {1, 2, 3}
two = {5, 6, 7}

newset = one.union(two)
print(newset)

# Keep only the duplicate
one = {1, 2, 3}
two = {2, 3, 4}

one.intersection_update(two)
print(one)

dupset = one.intersection(two)
print(dupset)

# Keep everything except the duplicate
one = {1, 2, 3}
two = {2, 3, 4}

one.symmetric_difference_update(two)
print(one)