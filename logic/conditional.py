score = 90
submitted_project = True

print("A" if score >= 90 else "")

if score >= 90:
    if submitted_project:
        print("A+")
    else:
        print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
elif score >= 60 or submitted_project:
    print("D")
else:
    print("F")


if score >= 90 and submitted_project:
    print("A+")
elif score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
elif score >= 60 or submitted_project:
    print("D")
else:
    print("F")

if score >= 90:
    print("High Score")
else:
    print("Low Score")

if submitted_project:
    print("Project is submitted")
else:
    print("Project is not submitted")

# Python Challange
# Validate the quality and correctness of email values
# must not be empty
# must contain "." and "@"
# must conatin exactly one "@" symbol
# must end with ".com" ".org" or ".net"
# must not be longer than 254 characters
# must start and end with letter or digit

email = "Peterfad20@gmail.net"
# print(email)
email = email.strip()
if email == "":
    print("Email cannot be empty")
elif email == None:
    print("Email cannot be none")
elif "." not in email:
    print("Email must have .")
elif email.count("@") != 1 :
    print("Email must have one @")
elif (email.endswith(".com") or email.endswith(".org") or email.endswith(".net")) == False:
    print("Email must have a domain name")
elif len(email) > 254:
    print("Email is too long")
else:
    print("Valid Email Address")


condition1 = email != "" and email != None and "." in email and "@" in email 
condition2 = email.endswith(".com") or email.endswith(".org") or email.endswith(".net")
condition3 = len(email) < 254
condition4 = email.count("@") == 1

# condition4 = (email.startswith(type(str)) or email.startswith(type(int))) and (
#     email.endswith(type(str)) or email.endswith(type(int)))


print(condition1 and condition2 and condition3 and condition4)

