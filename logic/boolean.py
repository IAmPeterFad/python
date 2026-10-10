# Value

print(True)
print(False)

# Function that return True and False
print(bool(123))
print(bool("Hi"))
print(bool())
print(bool(""))
print(bool(0))
print(bool(None))

email = "peterfad@gmail.com"
phone = "0172-342672"
username = ""

print(any([email, phone, username]))
print(all([email, phone, username]))
print("@gmail.com" in email)

print(isinstance(123, int))
print(isinstance(True, str))

"Hello".endswith("o")
"Hello".startswith("")

# Comparison Operation
print("-" * 10)

print(10 == 10)
print(10 != 10)
print(7 > 3)

print("a" == "A")
print("c" > "a")

# Is age between 18 and 30?
age = 24
print(18 <= age <= 30)
print(18 <= age and age <= 30)

if 18 <= age <= 30:
    print("I am a winner")
elif age < 18:
    print("Under age")
else:
    print("you are older")

# Logical Operation

print(3 > 5 and 7 > 5)
print(3 < 5 and 7 > 5)

print("~" * 10)

print(3 > 5 or 7 > 5)
print(3 < 5 or 7 > 5)
print(3 > 10 or 8 == 10)

# Check if the system is under pressure
cpu_usage = 70
memory_usage = 95

print(cpu_usage > 90 or memory_usage > 90)

# Checking users credentials before login
email = True
password = True

print(email and password)

# Not Operator
print("~" * 10)

print(3 > 2)
print( not 3 > 2)

print(not True)
print(not 0)
print(not 1)