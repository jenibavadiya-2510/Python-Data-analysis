# 1. Arithmetic Operators (+, -, *, /, //, %, **)
# Write a program to add two numbers.
# a = 10
# b = 20
# print(a+b)

# # Write a program to subtract two numbers.
# a = 10
# b = 20
# print(a-b)

# # Write a program to multiply two numbers.
# a = int(input("enter the value of a:"))
# b = int(input("enter the value of b:"))
# print("The mul of this two numbers are:", a*b)

# # Write a program to divide two numbers.
# a = 10
# b = 20
# c = a/b
# print(c)

# # # Find the remainder when 45 is divided by 8.
# # a = 45
# # b = 8
# # c = a%b
# # print(c)

# # Find the floor division of 50 and 6.
# a = 50
# b = 6
# c = a//b
# print(c)

# # Find the square of a number using the power operator.
# # Find the cube of a number.
# # Input the length and width of a rectangle and calculate its area.
# # Input the radius of a circle and calculate its area.

# # 2. Assignment Operators (=, +=, -=, *=, /=, //=, %=, **=)
# # Store 20 in a variable and add 15 using +=.
# x = 20
# x += 15
# print(x)

# # Store 100 in a variable and subtract 25 using -=.
# x = 100
# x -= 25
# print(x)

# # Multiply a variable by 5 using *=.
# x = int(input("enter the number:"))
# x *= 5
# print("Answer:", x)

# # Divide a variable by 4 using /=.
# y = int(input("enter the number:"))
# y /= 4
# print("Answer:", y)

# # Perform floor division using //=.
# x = int(input("enter the number:"))
# x //= 2
# print("Answer:", x)

# Find the remainder using %=.
# y = int(input("enter the number:"))
# y /= 50
# print("Answer:", y)

# Square a variable using **=.
# a = int(input("enter the number:"))
# a **= 4
# print("Answer:", a)

# Increase a variable by 1 using +=.
# num = int(input("enter the number:"))
# num += 1
# print("updated number:", num)

# Decrease a variable by 10 using -=.
# num = int(input("enter the number:"))
# num -= 1
# print("updated number:", num)

# Perform multiple assignment operations on the same variable and print the final value.

# 3. Comparison Operators (==, !=, >, <, >=, <=)
# Check whether two numbers are equal.
# a = int(input("enter the number:"))
# b = int(input("enter the number:"))
# print(a == b)

# Check whether two numbers are not equal.
# a = int(input("enter the number:"))
# b = int(input("enter the number:"))
# print(a != b)

# Check whether the first number is greater than the second.
# x = int(input("enter the number:"))
# y = int(input("enter the number:"))
# print(x>y)

# Check whether the first number is less than the second.
# x = int(input("enter the number:"))
# y = int(input("enter the number:"))
# print(x<y)

# Check whether a person's age is greater than or equal to 18.
# age = int(input("enter the age:"))
# print(age > 18)

# Check whether marks are less than 35.
# marks = int(input("enter the marks:"))
# print(marks < 35)

# Find the largest of two numbers.
# num1 = int(input("enter the number :"))
# num2 = int(input("enter the number :"))
# if num1 > num2:
#     print("num1 is greater than num2")
# else:
#     print("num2 is greater than num1")

# Check whether two strings are equal.
# str1 = input("enter the string1:")
# str2 = input("enter the string2:")
# if str1 == str2:
#     print("both string are equal")
# else:
#     print("string are not equal")

# Compare the salaries of two employees.
# salary1 = int(input("enter the salary :"))
# salary2 = int(input("enter the salary :"))
# if salary1 == salary2:
#     print("both employee salary are equal:")
# else:
#     print("salary are not equal:")

# Check whether a number is between 10 and 50.
# num = int(input("Enter the number: "))

# if num >= 10 and num <= 50:
#     print("Number is between 10 and 50")
# else:
#     print("Number is not between 10 and 50")

# 4. Logical Operators (and, or, not)

# Check whether a student has passed (marks > 35 and attendance > 75%).
# marks = int(input("enter the marks:"))
# attendence = int(input("enter the attendence:"))
# if marks >= 35 and attendence >= 75:
#    print("students is passed")
# else:
#    print("students is fail")

# Check whether a number is divisible by 2 or 5.
# num = int(input("Enter the number: "))

# if num % 2 == 0 or num % 5 == 0:
#     print("Number is divisible by 2 or 5")
# else:
#     print("Number is not divisible by 2 or 5")

# Check whether age is between 18 and 60.
# age = int(input("Enter the age: "))

# if age >= 18 and age <= 60:
#     print("Age is between 18 and 60")
# else:
#     print("Age is not between 18 and 60")

# Create a login system using username and password.
# username = input("Enter username: ")
# password = input("Enter password: ")

# if username == "admin" and password == "1234":
#     print("Login Successful")
# else:
#     print("Invalid Username or Password")

# Check whether a person is eligible for a loan (salary > 30000 and age > 21).
# salary = int(input("Enter salary: "))
# age = int(input("Enter age: "))

# if salary > 30000 and age > 21:
#     print("Eligible for Loan")
# else:
#     print("Not Eligible for Loan")

# Use not to reverse a Boolean value.
# is_active = True

# if not is_active:
#     print("User is inactive")
# else:
#     print("User is active")

# Check whether a number is positive and even.
# num = int(input("Enter number: "))

# if num > 0 and num % 2 == 0:
#     print("Number is positive and even")
# else:
#     print("Condition not satisfied")

# Check whether a number is negative or zero.
# num = int(input("Enter number: "))

# if num < 0 or num == 0:
#     print("Number is negative or zero")
# else:
#     print("Number is positive")

# Check whether a user is an admin and active.
# is_admin = input("Is user admin? ")
# is_active = input("Is user active? ")

# if is_admin == "yes" and is_active == "yes":
#     print("User is an active admin")
# else:
#     print("User is not an active admin")

# Check whether both conditions are False.
# condition1 = False
# condition2 = False

# if not condition1 and not condition2:
#     print("Both conditions are False")
# else:
#     print("Both conditions are not False")