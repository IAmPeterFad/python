users = ["Peter", "James", "Sarah"]

data = ["Peter", 24, True]

emptylist = []

print("Peter" in data)

print(users[0])
print(users[-1])

print(data.index(True))
print(users[0:])

print(len(users))

users.append("Elsa")
print(users)

users += ["Jason"]
print(users)

users.extend(["Michelle","Timi"])
print(users)

users.insert(0, "Jesus")
print(users)

users[2:2] = ["Eddie", "Alex"]
print(users)

users[1:3] = ["Robert", "JPJ"]
print(users)

users.remove("Robert")
print(users)

print(users.pop())
print(users)

del users[1]
print(users)

# del data
data.clear()
print(data)

users[1:2] = ["bola"]
users.sort()
print(users)

users.sort(key=str.lower)
print(users)

nums = [4,42,78,1,5]

nums.reverse()
print(nums)

# nums.sort(reverse= True)
# print(nums)

print(sorted(nums, reverse= True))
print(nums)

numscopy = nums.copy()
mynums = list(nums)
mycopy = nums[:]

print(numscopy)
mycopy.sort()
print(mynums)
print(mycopy)

print(type(nums))

mylist = list([1, "Neil", True])
print(mylist)

# Tuples

mytuple = tuple(("Dave", 42, True))
anothertuple = (1,3,4,5,2,7,2)

print(mytuple)
print(anothertuple)
print(type(mytuple) == tuple)
print(type(anothertuple) == tuple)

newlist = list(mytuple)
newlist.append("Neil")
newtuple = tuple(newlist)
print(newtuple)

(one, *two, hey) = anothertuple
print(one)
print(two)
print(hey)

print(anothertuple.count(2))