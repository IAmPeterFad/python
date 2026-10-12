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

# Dependent
email = "Peterfad20@gmail.com"
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
elif not email.endswith((".com",".org",".net")):
    print("Email end with .com, .org or .net")
elif len(email) > 254:
    print("Email is too long")
elif not(email[0].isalnum() and email[-1].isalnum()):
    print("Email must start or end with letter or digit")
else:
    print("Valid Email Address")

# Independent
valid = True
if email == "":
    print("Email cannot be empty")
    valid = False
if email == None:
    print("Email cannot be none")
    valid = False
if "." not in email:
    print("Email must have .")
    valid = False
if email.count("@") != 1 :
    print("Email must have one @")
    valid = False
if not email.endswith((".com",".org",".net")):
    print("Email end with .com, .org or .net")
    valid = False
if len(email) > 254:
    print("Email is too long")
    valid = False
if not(email[0].isalnum() and email[-1].isalnum()):
    print("Email must start or end with letter or digit")
    valid = False
if valid:
    print("Valid Email Address")


condition1 = email != "" and email != None and "." in email and "@" in email 
condition2 = email.endswith(".com") or email.endswith(".org") or email.endswith(".net")
email.endswith((".com",".org",".net"))
condition3 = len(email) < 254
condition4 = email.count("@") == 1


# print(condition1 and condition2 and condition3 and condition4)

# 2 Python Challenge 
# Validate the quality and correctness of a password
# must not be empty
# must be at least 8 characters
# must include at least 1 uppercase
# must include at least 1 lowercase
# must not be the same as the email
# must not contain any space
# must start and end with letter or digit

password = "Tryhackme"
# print(len(password))
# print(len(password) - len(password.strip()))

if password == "":
    print("Password can't be empty")
elif len(password) < 8:
    print("Password can't be less than 8 characters")
elif password == email:
    print("Password must not be the same as email")
elif len(password) != len(password.strip()):
    print("Password must not contain empty space")
elif not(password[0].isalnum() and password[-1].isalnum()):
    print("Password must start or end with letter or digit")
