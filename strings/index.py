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
first_name = "Micheal"
last_name = "Scott"
last_name = first_name + "-" + last_name
print(last_name)

folder = "C:/Users/Peter/"
file = "report.csv"
full_file_path = folder + file
print(full_file_path)

# f-string
name = "Sam"
age = 24
is_student = False

print("My name is", name, "I am", age, "years old, and student status is", is_student)
print(f"My name is {name}, I am {age}, years old, and student status is {is_student}.")

print(f"2 + 3 = {2 + 3}")
print(f"{{This is me}}")

# Split string
stamp = "2026-09-20 14:30"
print(stamp.split(" "))

stamp = "2026-09-20"
print(stamp.split("-"))

csv_file = "1234,Max,USA,1970-10-5,M"
print(csv_file.split(","))

# Multiple operation

print("ha" * 3)
print("~" * 50)

# Index and slicing
text = "Python"

print(text[0])
print(text[-1])

data = "2026-09-20"

# Extract the Year
print(data[0:4])

# Extract the Month
print(data[5:7])

# Extract the Day
print(data[8:])

# Whitespace Cleaning
Role = "  Engineering"
print(Role.lstrip())

Role = "Engineering ".rstrip()
print(Role)

text = "  Engineering    ".strip()
print(text)

text = "Data Engineering".strip()
print(text)

text = "####Abc####".strip("#")
print(text)

text = "      Engineering"
print(len(text))
print(len(text.strip()))

num_whitespace = len(text) - len(text.strip())
is_data_clean = len(text) == len(text.strip())

print(num_whitespace)
print(is_data_clean)

# Case Conversion
info = "Python PROGRAMMING"
print(info.lower())
print(info.upper())

search = "Email ".lower().strip()
data = "  email".lower().strip()

print(search == data)

# Challange
data = "968-Maria, (Data Engineer);; 27y "
new = data.replace("968-", "").replace(")", ",").replace("(", "").replace(";", "").replace("y", "").strip()
print(new.split(","))

# Search
phone = "+49-176-12345"
print(phone.startswith("+49"))

email = "peterfad@gmail.com"
print(email.endswith("@gmail.com"))
print("@" in email)

file = "data_backup.csv"
print(file.endswith(".csv"))

url = "https://api.company.com.v1.data"
print("/api." in url)

phone1 = "+48-176-12345"
phone2 = "48-365-12617"
phone3 = "0048-275-27818"

print(phone1[4:])
print(phone2[3:])
print(phone3[5:])

print(phone1.find("-"))

print(phone1[phone1.find("-")+1:])
print(phone2[phone2.find("-")+1:])
print(phone3[phone3.find("-")+1:])