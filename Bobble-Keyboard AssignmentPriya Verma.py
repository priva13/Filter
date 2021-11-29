# 1) Define a function which can generate a list where the values are square of numbers between 1 and 20 (both included). Then the function needs to print the first 5 elements in the list.

def printValues():
    l = list ()
    for i in range (1, 21):
        l.append (i ** 2)

    firstfive = l[:5]
    print (firstfive)


printValues ()

#2) Write a function to compute 5/0 and use try/except to catch the exceptions.

def divide():
    return 5/0

try:
    divide()
except ZeroDivisionError as ze:
    print("You are dividing a number by ZERO!!")
except:
    print("Any other exception")


#3) A website requires the users to input username and password to register. Write a program to check the validity o f password input by users.
#Following are the criteria for checking the password:
#1. At least 1 letter between [a-z]
#2. At least 1 number between [0-9]
#3. At least 1 letter between [A-Z]
#4. At least 1 character from [$#@]
#5. Minimum length of transaction password: 6
#6. Maximum length of transaction password: 12
#Your program should accept a sequence of comma separated passwords and will check them according to the above criteria. Passwords that match the criteria are to be printed, each separated by a comma.

user = input ()
passwords = user.split (",")
special = ["$", "#", "@"]
valid = []

for x in passwords:
    # check length
    if (len (x) > 12 or len (x) < 6):
        continue

    # check if has both uppercase and lower
    if (x.isupper () or x.islower ()):
        continue

    # check numbers
    has_number = any (char.isdigit () for char in x)
    if (not has_number):
        continue

    # check if has special character
    has_char = any (char in special for char in x)
    if (not has_char):
        continue

    # only reached if all checks are passed
    valid.append (x)
print (valid)


#4) Write a program which can filter even numbers in a list by using filter function. The list is: [1,2,3,4,5,6,7,8,9,10]

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print("\nEven numbers from the list:")
even_nums = list(filter(lambda x: x%2 == 0, nums))
print(even_nums)


# 5) Please write a program to generate all sentences where subject is in ["Aman", "He"] and verb is in ["Plays", "Likes"] and the object is in ["Volleyball","Ice-cream"].

subject=["Aman", "He"]
verb=["Playes", "Likes"]
obj=["Volleyball","Ice-cream"]

sentences = [(sub+" "+ vb + " " + ob) for sub in subject for vb in verb for ob in obj]
for sentence in sentences:
 print (sentence)


# 6) Assuming that we have some email addresses in the "username@companyname.com" format, please write program to print the user name of a given email address. Both user names and company names are composed of letters only.
# Example:
# If the following email address is given as input to the program: john@google.com
#  Then, the output of the program should be: john
#  In case of input data being supplied to the question, it should be assumed to be a console input

import re
email = "john@google.com"
mail = "(\w+)@\w+.com"
name = re.findall(mail,email)
print(name)
