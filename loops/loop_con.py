names = ["John", "Peter", "", "Joy"]

for name in names:
    if name == "":
        print("Name is empty")
        break
    print(f"Names = {name}")

for name in names:
    if name == "":
        print("Name is empty")
        continue
    print(f"Names = {name}")

for name in names:
    if name == "":
        pass  #todo: Handle Empty Value
    print(f"Names = {name}")

# Skips weekends in calender loop
days = ["Sun", "Mon", "Tue", "Wed", "Thur", "Fri", "Sat"]
weekends = ["Sun", "Sat"]

for day in days:
    if day in weekends:
        continue
    print(f"Workday: {day}")


emails = [
    "data@gmail.com", 
    "segun@outlook.com",
    "DRop Table User;",
    "sola@gmail.com"
]

for email in emails:
    if ";" in email:
        print("SQL Injection: Hacker Attack")
        break
    print(f"Processing Email: {email}")

# Else in loops
items = [1, 3, 5, 7]
for item in items:
    print(item)
else:
    print("Loop is completed")


items = [1, 3, 4, 7]
for item in items:
    if item % 2 == 0:
        print(f"Even num found: {item}")
        break
else:
    print("All numbers are odd")

names = ["Kinglesy", "Macus", "Marie", "Peace", "Prayer"]

for name in names:
    if name is None or name is "":
        print("Found a missing name")
        break
else:
    print("All names are available")

# Check if all files are csv

files = [
    "data.csv",
    "admin.txt",
    "class.csv",
    "note.pdf"
]

for file in files:
    if not file.endswith(".csv"):
        print("Not files are in csv format")
        break
else:
    print("All files are csv")


for file in files:
    if not file.endswith(".csv"):
        print(f"{file} is not in csv format")
        continue

# Python Challenge
# Check whether any filenames appears more than onces

file_list = [
    "report.csv",
    "data.xlsx",
    "summary.docx",
    "report.csv",
    "data.csv"
]

for file in file_list:
    if file == file:
        print("Duplicate found")
        break
else:
    print("All files are unique")