import math
# string data type

# literal assignment
first = "Peter"
last = "Fadokun"

print(type(first))
print(type(first) == str)
print(isinstance(first, str))

# construction function
pizza = str("pepperoni")

print(type(pizza))
print(type(pizza) == str)
print(isinstance(pizza, str))

# concatenation

fullname = first + " " + last
print(fullname)

fullname += "!"
print(fullname)

# Casting a number to a string
decade = str(1980)
print(type(decade) == str)
print(decade)

statement = "I like Rock music from the " + decade + "S."
print(statement)

# Mutiple lines
mutiline = '''
Hey, how are you?

I was just checking in.
                               All good?

'''
print(mutiline)

# Escaping special characters
sentance = 'I\'m back at work!\tHey!\n\nWhere\'s this at\\located?'
print(sentance)

# String Method
print(first)
print(first.lower())
print(first.upper())

print(mutiline.title())
print(mutiline.replace("good", "ok"))
print(mutiline)

# Build a Menu
title = "menu".upper()
print(title.center(20, "="))
print("Coffee".ljust(16, ".") + "$1".rjust(4))
print("Muffin".ljust(16, ".") + "$2".rjust(4))
print("Cheesecake".ljust(16, ".") + "$4".rjust(4))

#string index values
print(first[0])
print(first[1])
print(first[-1])
print(first[0:])

# Some method reture boolean data
print(first.startswith("P"))
print(first.endswith("r"))

#Boolean data type
myvalue = True
x = bool(False)

print(type(x))
print(type(myvalue) == bool)
print(isinstance(x, bool))

# Numeric data type

#integer type
price = 100
best_price = int(80)

print(type(price))
print(isinstance(best_price, int))

# Float type
gpa = 3.28
y = float(1.14)

print(type(gpa))

# Complex type
comp_value = 5 + 3j
print(type(comp_value))
print(comp_value.real)
print(comp_value.imag)

# Built-in functions for numbers
print(abs(gpa))
print(abs(gpa * -1))
print(round(gpa))
print(round(gpa, 1))

print(math.pi)
print(math.sqrt(64))
print(math.ceil(gpa))
print(math.floor(gpa))

# Casting a string to a number
zipcode = "10001"
zip_value = int(zipcode)

print(type(zipcode))
print(type(zip_value))