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


