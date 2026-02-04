# 1. Check if a number is positive or negative
num = int(input("Enter a number: "))

if num > 0:
    print("Positive number")
else:
    print("Negative number")


# 2. Check if a number is even or odd
num = int(input("Enter a number: "))

if num % 2 == 0:
    print("Even number")
else:
    print("Odd number")


# 3. Find the greater of two numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if a > b:
    print("A is greater")
else:
    print("B is greater")


# 4. Check if a person is eligible to vote
age = int(input("Enter your age: "))

if age >= 18:
    print("Eligible to vote")
else:
    print("Not eligible to vote")


# 5. Check if a number is divisible by 5
num = int(input("Enter a number: "))

if num % 5 == 0:
    print("Divisible by 5")
else:
    print("Not divisible by 5")


# 6. Find the grade based on marks
marks = int(input("Enter marks: "))

if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 50:
    print("Grade C")
else:
    print("Fail")


# 7. Check whether a year is a leap year
year = int(input("Enter a year: "))

if year % 4 == 0:
    print("Leap year")
else:
    print("Not a leap year")


# 8. Check if a number is zero or non-zero
num = int(input("Enter a number: "))

if num == 0:
    print("Number is zero")
else:
    print("Number is non-zero")


# 9. Find the largest of the three numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a > b and a > c:
    print("A is largest")
elif b > c:
    print("B is largest")
else:
    print("C is largest")


# 10. Simple login check
username = input("Enter username: ")
password = input("Enter password: ")

if username == "admin" and password == "1234":
    print("Login successful")
else:
    print("Login failed")
