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

# Allow access only if the user is login or guest
# They must not be banned user

is_logged_in = True
is_guest = False
is_banned = True

print((is_logged_in or is_guest) and not is_banned)

# Membership Operation
print("o" in "python")
print(3 not in [1,2,3,4,5])

# Ensure the domain is not banned
domain = "spam.com"
banned = ["spam.com", "fake.net", "bot.net"]

print(domain not in banned)

# Identity Operators
x = ["a", "b", "c", "d"]
y = ["a", "b", "c", "d"]

print(x is y)
print(x == y)

a = "Peter"
b = "Peter"

print(a is b)

x = ["a", "b", "c", "d"]
y = x

print(x == y)
print(x is y)

# Ensure the email exit
email = "Peterfad20@gmail.com"
print(email != None and email != "" and "@gmail.com" in email)

# username is not empty and the age is greater than or equal 18
user = "Sola"
age = 17

print((user is not "" and user is not None) and age >= 18)

# password is 8 character long and does not contain space
password = "Tryhack "

print(len(password) >= 8)
print(len(password.strip()) >= 8)


# user email is not empty, contain @ and end with .com
email = "peterfad20@gmail.com"

print((email is not "" and email is not None) and email.endswith(".com") and "@" in email)
# user is string, is not None and is longer than 5 characters
user = "Peterfad"
print(len(user) > 5 and user is not None and isinstance(user,str) )
# user is an admin or moderator and either they are not banned and have verified their mail
admin = False
moderator = False
banned = True
verified = False


