#Type
name = "Peter"
print(type(name))

age = 24
print(type(age))
print("Your age is: " + str(age))
print(type(age))
age = str(age)
print(type(age))

# Math
password = "123a2262423"
print(len(password))

if len(password) < 8:
    print("Your password is too short!")

text = """
Python is easy to learn.
Python is powerful$.
Many people love python.
"""
print(text.count("Python"))
print(text.count("$"))

# Transformation
price = "1234,56"
print(price.replace(",", "."))

phone = "176-2462-23"
print(phone.replace("-", "/"))
print(phone.replace("-", ""))

price = "$1,299.90"
print(price.replace("$", "").replace(",", ""))

num = "+49 (176) 123-4567"
phone = num.replace("+", "00").replace("(","").replace(")","").replace("-", "").replace(" ", "")
print(phone)

# Join string