# if-else statement

# Basic — 
# Write a program to check whether a number is positive or negative.
# num = int(input("enter the number:"))
# if(num > 1):
#     print("positive")
# else :
#     print("negative")

# Write a program to check whether a number is even or odd.
# num = int(input("enter the number:"))
# if num % 2 == 0:
#     print("even")
# else :
#     print("odd")

# Take a student's marks. If marks are 40 or above, print "Pass", otherwise print "Fail".
# marks = int(input("enter the marks:"))
# if marks >= 40:
#     print("Pass")
# else :
#     print("Fail")

# Take a person's age. If age is 18 or above, print "Eligible to Vote", otherwise print "Not Eligible".
# age = int(input("enter your age:"))
# if age >= 18:
#     print("Eligible for vote")
# else :
#     print("Not eligible for vote")

# Take two numbers and print which number is greater.
# num1 = 20
# num2 = 45
# if num1 > num2:
#     print("num1 is greater")
# else :
#     print("num2 is greater")

# Take two numbers and check whether they are equal or not.
# num1 = int(input("enter the number1 :"))
# num2 = int(input("enter the number2 :"))
# if num1 == num2:
#     print("Both are equal")
# else :
#     print("Both are not equal")

# Take a number and check whether it is divisible by 5 or not.
# num = int(input("enter the number :"))
# if num % 5 == 0:
#     print("Divisible by 5")
# else :
#     print("Not divisible by 5")

# Take a number and check whether it is greater than 100 or not.
# num = int(input("enter the number :"))
# if num > 100:
#     print("The number is greater than 100")
# else :
#     print("The number is not greater than 100")

# Take a temperature. If it is 30 or above, print "Hot", otherwise print "Normal".
# temperature = int(input("enter the tem :"))
# if temperature >= 30 :
#     print("The weather is Hot")
# else :
#     print("The weather is normal")

# Take a password. If the password is "python123", print "Correct Password", otherwise print "Wrong Password".
# password = input("enter the password :")
# if password == "python123":
#     print("correct passwrod")
# else:
#     print("wrong password")

# Medium — 11 to 20
# Take a number and check whether it is divisible by both 5 and 10.
# num = int(input("enter the number :"))
# if num % 5 == 0 and num % 10 == 0:
#     print("The number is divisible by both")
# else:
#     print("The number is not divisible by both")

# Take a student's marks. If marks are 70 or above, print "Good", otherwise print "Needs Improvement".
# marks = int(input("enter the marks :"))
# if (marks >= 70):
#     print("Good")
# else :
#     print("Needs improvement")

# Take a shopping amount. If the amount is ₹5000 or above, give a 10% discount, otherwise give a 5% 
# discount.
# amount = int(input("enter the amount :"))

# if (amount >= 5000):
#     discount = amount - (amount * 0.10)
#     print("total amount are :",discount)

# else:
#     discount = amount - (amount * 0.05)
#     print("total amount are :",discount)
  
# Take a person's age. If age is 13 or above, print "Teenager", otherwise print "Not a Teenager".
# age = int(input("enter the age :"))
# if age >= 13:
#     print("Teenager")
# else :
#     print("Not a teenager")

# Take three numbers and print the largest number.
# num1 = int(input("enter the number :"))
# num2 = int(input("enter the number :"))
# num3 = int(input("enter the number :"))
# if (num1 >= num2 and num1 >= num3):
#     print("num1 is greater then two number")
# elif (num2 >= num1 and num2 >= num3):
#     print("num2 is greater then two number")
# else:
#     print("num3 is greater then two number")

# Take three numbers and print the smallest number.
# num1 = int(input("enter the number :"))
# num2 = int(input("enter the number :"))
# num3 = int(input("enter the number :"))
# if (num1 <= num2 and num1 <= num3):
#     print("num1 is less then two number")
# elif (num2 <= num1 and num2 <= num3):
#     print("num2 is less then two number")
# else:
#     print("num3 is less then two number")

# Take a username and password. If username is "admin" and password is "1234", print "Login Successful",
#  otherwise print "Invalid Login".
# username = input("enter the username :")
# password = int(input("enter the password :"))
# if (username == "admin" and password == 1234):
#     print("Login successful")
# else :
#     print("Invalid login")

# Take electricity units. If units are 100 or less, charge ₹5 per unit; otherwise charge ₹7 per unit.
#  Print the total bill.
# units = int(input("enter the units :"))
# if (units <= 100):
#     bill = units * 5
# else:
#     bill = units * 7
# print("Total bill:", bill)

# Take a student's attendance percentage. If attendance is 75 or above, print "Allowed for Exam", 
# otherwise print "Not Allowed".
# attendance = int(input("enter the attendance :"))
# if (attendance >= 75):
#     print("Allowed for exam")
# else :
#     print("Not allowed")

# Take a number and check whether it is positive and even or otherwise.
# num = int(input("enter the number :"))
# if (num > 0 and num % 2==0):
#     print("Positive and even")
# else:
#     print("otherwise")

# if-elif-else

# Student Grade System
# Take marks and print the grade: A+, A, B, C, D, or F according to the marks range.

# marks = int(input("enter the marks :"))
# if marks >= 95:
#     print("Grade A+")
# elif marks >= 90:
#     print("Grade A")
# elif marks >= 80:
#     print("Grade B")
# elif marks >= 70:
#     print("Grade C")
# elif marks >= 60:
#     print("Grade D")
# else :
#     print("Grade F")

# Electricity Bill
# Take units and calculate the bill using different rates for 0–100, 101–200, 201–300, and above 300 
# units.

# units = int(input("enter the units :"))
# if units <= 100:
#     bill = units * 5
# elif units <= 200:
#     bill = units * 7
# elif units <= 300:
#     bill = units * 10
# else :
#     bill = units * 15
# print("Total bill:", bill)

# Shopping Discount
# Take the purchase amount and apply different discounts for different amount ranges. 
# Print the final amount.

# amount = int(input("enter the amount :"))

# if amount >= 10000:
#     discount = amount - (amount * 0.10)
# elif amount >= 5000:
#     discount = amount - (amount * 0.05)
# elif amount >= 500:
#     discount = amount - (amount * 0.02)
# else :
#     discount = amount
# print("total amount:", discount)

# Employee Bonus
# Take salary and years of experience. Give different bonus percentages based on experience.

# Experience = int(input("enter the experience_years :"))
# salary = int(input("Enter the salary :"))
# if Experience >= 10:
#     bonus = salary * 0.20
# elif Experience >= 5:
#     bonus = salary * 0.10
# elif Experience >= 2:
#     bonus = salary * 0.50
# else :
#     bonus = salary * 0.02
# print("bonus :", bonus)
# print("Total salary :", salary + bonus)

# Income Tax Calculator
# Take annual income and calculate tax according to different income slabs.

# annual_income = int(input("Enter the income :"))
# if annual_income >= 2000000:
#     tax = annual_income * 0.20
# elif annual_income >= 1500000:
#     tax = annual_income * 0.15
# elif annual_income >= 800000:
#     tax = annual_income * 0.10
# elif annual_income >= 400000:
#     tax = annual_income * 0.05
# else :
#     tax = annual_income * 0
# print("annual_income :", annual_income)
# print("tax", tax)

# Movie Ticket Pricing
# Take age and calculate ticket price according to child, teenager, adult, and senior-citizen 
# categories.

# age = int(input("enter the age:"))

# if age <= 12:
#     ticket_price = 100
# elif age <= 17:
#     ticket_price = 150
# elif age <= 50:
#     ticket_price = 200
# else:
#     ticket_price = 120
# print("ticket_price", ticket_price)

# Loan Eligibility
# Take salary, age, and credit score. Decide whether the customer is eligible, conditionally 
# eligible, or not eligible for a loan.

# salary = int(input("Enter the salary:"))
# age = int(input("Enter the age :"))
# credit_score = int(input("Enter the score :"))
# if salary >= 50000 and age >= 30 and credit_score >= 700:
#     print("Loan Eligible")
# elif salary >= 25000 and age >= 35 and credit_score >= 650:
#     print("Conditionally Eligible ")
# else :
#     print("Not eligible for a loan")


# Email validation
# Email = input("Enter your email : ")

# if("@" in Email and "." in Email and " " not in Email):
#     print("Your email is valid")
# else:
#     print("your email is worng")


# Triangle Classification
# Take three sides. First check whether the triangle is valid, then classify it as Equilateral, 
# Isosceles, or Scalene.

# Num1 = int(input("Enetr a Number: "))
# Num2 = int(input("Enetr a Number: "))
# Num3 = int(input("Enetr a Number: "))
# if Num1 == Num2 == Num3:
#     print("Triangle is Equilateral")
# elif Num1 == Num2 or Num1 == Num3 or Num2 == Num3:
#     print("Triangle is Isosceles")
# else:
#     print("Triangle is Scalene") 

# Number Classification
# Take a number and classify it as:
# Positive Even
# Positive Odd
# Negative Even
# Negative Odd
# Zero

# Number = int(input("Enter the number:"))
# if Number > 0 and Number % 2 != 0:
#     print("positive odd")
# elif Number > 0 and Number % 2 == 0:
#     print("positive even")
# elif Number < 0 and Number % 2 == 0:
#     print("negative even")
# elif Number < 0 and Number % 2 != 0:
#     print("negative odd")
# else:
#     print("zero")

# Online Shopping Delivery Charge
# Take order amount and membership type. Calculate delivery charges based on different combinations.

# order_amount = int(input("enter the order_amount :"))
# membership_type = input("enter the type :")
# if order_amount >= 5000 and membership_type == "Gold":
#     delivery = 0
# elif order_amount >= 5000 and membership_type == "Silver":
#     delivery = 50
# else:
#     delivery = 100
# print("delivery charge:", delivery)

# Employee Performance Rating
# Take performance score and years of experience. Give ratings such as Excellent, Good, Average,
#  or Poor based on the conditions.

# score = int(input("enter the score :"))
# Experiance = int(input("Enter the Experience :"))
# if score > 90 and Experiance > 3:
#     print("Excellent")
# elif score > 75 and Experiance > 2:
#     print("Good")
# elif score > 60:
#     print("Average")
# else:
#     print("Poor")


# Parking Fee Calculator
# Take parking hours and vehicle type. Calculate the parking fee according to different time and 
# vehicle categories.

# parking_hours = int(input("enter the hours :"))
# vehicle_type = input("enter the vehicle_name :")
# if parking_hours >= 2 and vehicle_type == "Bike":
#     charge = parking_hours * 20
# elif parking_hours >= 5 and vehicle_type == "car":
#     charge = parking_hours * 50
# elif parking_hours >= 10 and vehicle_type == "Truck":
#     charge = parking_hours * 100
# else :
#     charge = parking_hours * 150
# print("Charge", charge)

# Exam Eligibility System
# Take attendance percentage, assignment status, and internal marks. Decide whether the student is
#  Eligible, Conditionally Eligible, or Not Eligible.

# attendance_percentage = int(input("enter the percentage :"))
# assignment_status = input("enter the status :")
# if attendance_percentage >= 75 and assignment_status == "submitted":
#     print("Eligible")
# elif attendance_percentage >= 75 and assignment_status == "not submitted":
#     print("Conditinally eligible")
# else :
#     print("Not eligible")

# Bank Account Transaction
# Take account type, balance, and transaction amount. Decide whether the transaction is valid, 
# rejected, or successful according to account rules.

# account_type = input("Enter account type: ")
# balance = int(input("Enter account balance: "))
# amount = int(input("Enter transaction amount: "))

# if account_type != "Savings" and account_type != "Current":
#     print("Invalid Account")

# elif amount <= 0:
#     print("Invalid Amount")

# elif amount > balance:
#     print("Insufficient Balance")

# else:
#     balance = balance - amount
#     print("Transaction Successful")
#     print("Remaining Balance:", balance)

# nested if-else 

# Basic
# # Take a number. First check whether it is positive. If positive, check whether it is even or odd.
# num = int(input("enter the number :"))
# if num > 0:
#     if num % 2 == 0:
#          print("positive and even")
#     else:
#          print("positive and odd")
# else:
#      print("number is not positive")


# Take age. First check whether the person is eligible to vote. If eligible, check whether the
#  person is a first-time voter.
# age = int(input("enter the age:"))
# first_time = input("Is this your first time voting?")
# if age > 18:
#     if first_time == "yes":
#         print("eligible and first time voter")
#     else:
#         print("eligible for vote")
# else:
#     print("not eligible to vote ")

# Take marks. First check whether the student passed. If passed, check whether marks are above 75.
# marks = int(input("enter the marks:"))
# pass_value = input("student passed?")
# if pass_value == "pass":
#     if marks > 75:
#         print("Student passed and marks are above 75")
#     else:
#         print("Student passed but marks are 75 or below")
# else:
#     print("Student is not passed")

# Take a number. First check whether it is greater than 50. If yes, check whether it is even or odd.
# num = int(input("enter the number :"))
# if num > 50:
#     if num%2 == 0:
#         print("The number is greater than 50 and even")
#     else :
#         print("The number is greater than 50 and odd")
# else:
#     print("The number is not greater than 50")

# 🟡 Intermediate
# Take username and password. First check whether the username is correct. If correct, check whether
# the password is correct.
# username = input("enter username :")
# password = input("enter password :")
# if username == "admin":
#     if password == "12345":
#         print("login successful")
#     else :
#         print("incorrect password")
# else:
#     print("incorrect username")

# Take account balance and withdrawal amount. First check whether the account has sufficient balance.
#  If yes, check whether the withdrawal amount is a multiple of 100.
# balance = int(input("Enter account balance: "))
# withdrawal = int(input("Enter withdrawal amount: "))
# if withdrawal <= balance:
#     if withdrawal % 100 == 0:
#         balance = balance - withdrawal
#         print("Withdrawal Successful")
#         print("Remaining Balance:", balance)
#     else:
#         print("Invalid Withdrawal Amount")
# else:
#     print("Insufficient Balance")

# Take age and nationality. First check whether the person is an Indian citizen. If yes, 
# check whether they are eligible to vote based on age.
# age = int(input("Enter the age:"))
# nationality = input("enter the nationality :")
# if nationality == "Indian citizen":
#     if age >= 18:
#         print("Eligible for vote and is an indian citizen")
#     else:
#         print("Not eligible for vote and is an indian citizen")
# else:
#     print("Not an indian citizen")


# Take salary and years of experience. First check whether salary is at least ₹30,000. If yes, 
# check whether experience is at least 2 years.
# salary = int(input("enter the salary:"))
# experience = int(input("enter the experience :"))
# if salary >= 30000:
#     if experience >= 2:
#         print("Eligible")
#     else:
#         print("Not eligible due to low experience")
# else:
#     print("Not eligible due to low salary")

# Take a shopping amount and membership type. First check whether the amount is at least ₹5,000.
#  If yes, check whether the customer is a Gold member.
# amount = int(input("enter the amount :"))
# membership_type = input("enter the membership_type :")
# if amount >= 5000:
#     if membership_type == "Gold":
#        print("customer is eligible for gold discount")
#     else:
#         print("customer is not gold member")
# else :
#     print("Amount is less than 50000")

# Take a number. First check whether it is positive. If positive, check whether it is greater than 
# 100; otherwise check whether it is even or odd.

# num = int(input("Enter the number: "))
# if num > 0:
#     if num > 100:
#         print("Positive and greater than 100")
#     else:
#         print("Positive but not greater than 100")
# else:
#     if num % 2 == 0:
#         print("Not positive and even")
#     else:
#         print("Not positive and odd")

# 🔴 Advanced
# ATM System
# Take PIN and withdrawal amount. First check whether the PIN is correct. If correct, check whether the amount is 
# valid. If valid, check whether sufficient balance is available.

# pin = int(input("enter the pin :"))
# withdrawal_amount = int(input("enter the amount :"))
# balance = int(input("enter the balance :"))
# if pin == 1234567:
#     if withdrawal_amount > 0:
#         if withdrawal_amount <= balance:
#           print("withdrawal is successful:")
#         else :
#           print("insufficient balance:")
#     else:
#       print("invalid withdrawal amount:")
# else:
#    print("incorrect pin")

# Loan Eligibility
# Take salary, age, and credit score. First check whether age is within the allowed range. If yes, check salary. 
# If salary is sufficient, check the credit score.

# salary = int(input("Enter the salary:"))
# age = int(input("Enter the age :"))
# credit_score = int(input("Enter the score :"))
# if age >= 18:
#     if salary >= 10000:
#         if credit_score >= 350:
#             print("Loan eligible")
#         else:
#             print("loan is not eligible due to low score")
#     else:
#         print("loan is not eligible due to low salary")
# else:
#     print("Not required age")


# Online Shopping
# Take order amount and membership. First check whether the order amount qualifies for a discount. If yes, 
# check membership type and apply the appropriate discount.
# order_amount = int(input("enter the amount :"))
# membership_type = input("enter the membership_type :")
# if order_amount >= 5000:
#     if membership_type == "Gold":
#         discount = order_amount * 0.20
#         print("Gold member - 20% discount")
#         print("Discount:", discount)
#     else:
#         discount = order_amount * 0.10
#         print("10% discount")
#         print("Discount:", discount)
# else:
#     print("No discount")

# Bank Transaction
# Take account type, balance, transaction amount, and PIN. First verify the PIN. If correct, check the account type.
#  If valid, check the balance and then approve or reject the transaction.
# account_type = input("Enter account type: ")
# balance = int(input("Enter account balance: "))
# amount = int(input("Enter transaction amount: "))
# pin = int(input("enter the pin:"))

# if pin == 11223344:
#     if account_type == "Savings" or account_type == "Current":
#        if amount <= balance:
#            balance = balance - amount
#            print("Transaction approved")
#            print("Remaining balance:", balance)
#         else:
#            print("Transaction rejected: insufficient balance:")
#     else:
#         print("Invalid account type:")    
# else:
#     print("incorrect pin")



