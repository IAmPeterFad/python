count = 1
while count <= 5:
    print(count)
    count += 1

answer = ""
while answer != "yes":
    answer = input("Do you agree?(yes/no): ")
print("Thank you")

while True:
    answer = input("Do you agree?(yes/no): ")
    if answer == "yes":
        break
print("Thank You")


# 3 attempts

attempts = 0

while attempts < 3:
    answer = input("Do you agree?(yes/no): ")
    if answer == "yes":
        print("Glad we're on the same page")
        break
    attempts += 1
else:
    print("3 strikes. You're out!")