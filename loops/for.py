
# print("Round: 1")
# print("Round: 2")
# print("Round: 3")
# print("Round: 4")
# print("Round: 5")

for i in (1,2,3,4,5):
    print(f"Round: {i}")

items = ("A","B","C","D","E")

for item in items:
    print(f"Round: {item}")


items = "Python"

for item in items:
    print(f"Round: {item}")


for item in range(3):
    print(f"Round: {item}")

for item in range(1,5):
    print(f"Round: {item}")

for item in range(0,10,2):
    print(f"Round: {item}")

scores = [80, 50, 65, 73]
total = 0

for score in scores:
    total = total + score
    print(f"Current Total: {total}")

print(f"Final Total: {total}")

# clear data
# Inconsistency casing and unnecessary spaces
files = [" Report.csv  ", "DATA.csv   ", "  Final.TXT"]

for file in files:
    file = file.strip().lower().replace(".txt", ".csv")
    print(f"Processing {file}")

# 7 times-table using for loop from 1-10
for x in range(1,11):
    print(f"7 x {x} = {x * 7}")

