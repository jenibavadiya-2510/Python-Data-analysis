# try:
#     print(10/0)
# except:
#     print("0 is not divisible")

# basic question

# Write a Python program to handle ZeroDivisionError when dividing two numbers.
# try:
#     print(10/0)
# except:
#     print("not divisible")
# finally:
#     print("not run")

# Write a program that takes an integer from the user and handles ValueError 
# if the user enters text.
# try:
#     num = int(input("enter a number:"))
#     print("number is:", num)
# except ValueError:
#     print("please enter a valid integer")

# Write a program to access an element from a list and handle IndexError.
# numbers = [10, 20, 30, 40, 50]
# try:
#     print(numbers[30])
# except IndexError:
#     print("index is out of range")

# Write a program to access a key from a dictionary and handle KeyError.
# student = {
#     "name": "Jeni",
#     "age": 21,
#     "course": "Python"
# }

# try:
#     print(student["marks"])
# except KeyError:
#     print("Key not found in dictionary")


# student marks
# try:
#     marks = int(input("enter the marks:"))

#     if marks < 0 or marks > 100:
#         raise ValueError("please enter correct marks")

# except ValueError as e:
#     print(e)

# else:
#     print("valid marks")

# else code
# try:
#     num1 = int(input("enter number :"))
#     num2 = int(input("enter number :"))
#     print(num1/num2)

# except ZeroDivisionError:
#     print("0 thi divide")

# else:
#     print("code run perfectly")

# number input
# try:
#     age = int(input("enter age:"))
# except ValueError:
#     print("please enter number only")

# # claculator system
# try:
#     print("1. add")
#     print("2. subtract")
#     print("3. multiplication")
#     print("4. divide")

#     num1 = int(input("enter the number:"))
#     num2 = int(input("enter the number:"))

#     choice = int(input("enter number :"))

#     if choice == 1:
#         print(num1 + num2)

#     if choice == 2:
#         print(num1-num2)

#     if choice == 3:
#         print(num1*num2)

#     if choice == 4:
#         print(num1/num2)

# except ZeroDivisionError:
#     print("not divide by zero")

# 1. ATM System

# Write a Python program where the user enters a withdrawal amount.
# If the amount is less than or equal to 0, raise a ValueError. Otherwise, 
# print "Withdrawal successful".

# try:
#     amount = int(input("enter the amount :"))

#     if amount <= 0:
#         raise ValueError("please enter positive amount")

# except Exception as e:
#     print(e)

# else:
#     print("withdrawal amount")

# 2. Bank Account

# Write a Python program where the user enters an account balance and withdrawal amount.
# If the withdrawal amount is greater than the balance, raise a ValueError("Insufficient balance").
#  Otherwise, print "Transaction successful".

# try:
#     account_balance = int(input("enter the balance :"))
#     amount = int(input("enter the amount :"))

#     if amount > account_balance:
#         raise ValueError("Insufficient balance")

# except Exception as e:
#     print(e)

# else: 
#     print("Transaction successful")


# 3. Online Shopping

# Write a Python program where the user enters product quantity.
# If the quantity is less than 1 or greater than 10, raise a ValueError("Invalid quantity"). 
# Otherwise, print "Order placed successfully".

# try:
#     quantity = int(input("enter the product quantity :"))

#     if quantity < 1 or quantity > 10:
#         raise ValueError("Invalid quantity")

# except Exception as e:
#     print(e)

# else:
#     print("order placed successfully")


# 4. Student Registration

# Write a Python program where the user enters student age.
# If the age is less than 5 or greater than 100, raise a ValueError("Invalid age"). Otherwise, 
# print "Registration successful".
# try:
#     age = int(input("enter the age :"))

#     if age < 5 or age > 100:
#         raise ValueError("Invalid age")

# except Exception as e:
#     print(e)

# else:
#     print("Registration successful")


# 5. Mobile Recharge

# Write a Python program where the user enters a mobile number and recharge amount.
# If the mobile number is not 10 digits, raise a ValueError("Invalid mobile number"). 
# Otherwise, print "Recharge successful".
# try:
#     mobile_number = input("enter the number :")
#     amount = int(input("enter recharge amount :"))

#     if len(mobile_number) != 10:
#         raise ValueError("Invalid mobile number")

#     if amount <= 0:
#         raise ValueError("Invalid recharge amount")

# except Exception as e:
#     print(e)

# else:
#     print("Recharge successful")
