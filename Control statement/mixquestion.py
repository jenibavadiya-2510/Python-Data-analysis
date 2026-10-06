# Check if a number is positive or negative.
# number = int(input("enter number :"))

# if number > 0:
#     print("positive number")
# else:
#     print("negative number")

# # Check if a number is even or odd.
# number = int(input("enter number :"))

# if number%2==0:
#     print("even number")
# else:
#     print("odd number")

# # Find the greater of two numbers.
# number1 = int(input("enter number :"))
# number2 = int(input("enter number :"))

# if number1 > number2:
#     print("number 1 is great")
# else:
#     print("number2 is great")

# # Find the smaller of two numbers.
# number1 = int(input("enter number :"))
# number2 = int(input("enter number :"))

# if number1 < number2:
#     print("number 1 is small")
# else:
#     print("number2 is small")

# # Check whether a number is divisible by 5.
# number = int(input("enter number :"))

# if number%5==0:
#     print("divisible by 5")
# else:
#     print("not divisible by 5")
    
# # Check whether a person is eligible to vote (age ≥ 18).
# age = int(input("enter age :"))

# if age >= 18:
#     print("eligible for vote")
# else:
#     print("not eligible for vote")

# # Check whether a year is a leap year.
# year = int(input("Enter the year :"))
# if year % 4 == 0:
#     print("Leap year")
# else:
#     print("Not a leap year")

# # Check whether a character is a vowel or consonant.
# character = input("enter the character :")
# if character in "aeiou":
#     print("This is vowel")
# else :
#     print("This is consonant")

# # Check whether a number is a multiple of 3.
# number = int(input("enter the number :"))
# if number % 3 == 0:
#     print("number is multiple of 3")
# else:
#     print("number is not multiple of 3")

# # Check whether a student has passed (marks ≥ 35).
# marks = int(input("Enter the number :"))
# if marks >= 35:
#     print("students has passed")
# else:
#     print("student has fail")

# # Find the largest of three numbers.
# num1 = int(input("enter the number1:"))
# num2 = int(input("enter the number2:"))
# num3 = int(input("enter the number3:"))
# if num1 > num2 and num1 and num3:
#     print("num1 is large")
# elif num2 > num3 and num2 > num1:
#     print("num2 is large")
# else:
#     print("num3 is large")

# # Find the smallest of three numbers.
# num1 = int(input("enter the number1:"))
# num2 = int(input("enter the number2:"))
# num3 = int(input("enter the number3:"))
# if num1 < num2 and num1 < num3:
#     print("num1 is smallest")
# elif num2 < num3 and num2 < num1:
#     print("num2 is smallest")
# else:
#     print("num3 is smallest")

# # Check whether a number is a 2-digit, 3-digit, or 4-digit number.
# number = int(input("enter the number :"))
# if number >= 10 and number <= 99:
#     print("number is 2-digits")
# elif number >= 100 and number <= 999:
#     print("number is 3-digits")
# else:
#     print("number is 4-digits")

# # Check whether a character is uppercase or lowercase.
# text = input("enter the text:")
# if text.isupper:
#     print("text is uppercase")
# else:
#     print("text is lowercase")

# # Check whether a character is an alphabet, digit, or special character.
# character = input("enter text :")

# if ("a" <= character <= "z") or ("A" <= character <= "Z"):
#     print("alphabet")

# elif ("0" <= character <= "9"):
#     print("digit")

# else:
#     print("special character")

# # Check whether a number is divisible by both 3 and 5.
# number = int(input("enter number :"))

# if number%3 == 0 and number%5 == 0:
#     print("divisible by both")

# else:
#     print("not divisible")

# # Check whether a person is a child, teenager, adult, or senior citizen.
# age = int(input("enter age :"))

# if age >= 1 and age <= 10:
#     print("child")

# elif age > 10 and age <= 21:
#     print("Teenager")

# elif age > 21 and age <= 60:
#     print("Adult")

# else:
#     print("senior citizen")


# # Find the absolute value of a number.
# number = int(input("enter number :"))

# if number < 0 :
#     print(-number)
# else:
#     print(number)

# # Check whether a number lies between 1 and 100.
# number = int(input("enter number :"))

# if number >= 1 and number <= 100:
#     print("lies between 1 to 100")
# else:
#     print("not lies")

# # Check login using username and password.
# username = "jeni263"
# password = 123456

# uname = username
# upass = password

# username = input("enter username :")

# if username == uname:
#     print("username valid")

#     password = int(input("enter password :"))

#     if password == upass:
#         print("login sucessfull")
#     else:
#         print("enter valid password")
    
# else:
#     print("Invalid username")

# # ATM withdrawal (balance and PIN validation).
# amount = 56000
# correct_pin = "123456"
# balance = int(input("enter balance :"))

# if balance < amount:
#     print("sufficient balance")

#     ATM_PIN = input("enter pin :")

#     if len(ATM_PIN) >= 6:
#         if ATM_PIN == correct_pin:
#             print("transaction sucessful")
#         else:
#             print("incorrect pin")

#     else:
#         print("please enter 6 digit pin") 

# else:
#     print("insufficient balance")


# # Check whether a student passed all subjects.
# english = int(input("enter english marks :"))
# hindi = int(input("enter hindi marks :"))
# science = int(input("enter science marks :"))

# if english >= 35 and hindi >= 35 and science >= 35:
#     print("Student passed all subjects")
# else:
#     print("Student failed")


# # Find the greatest of four numbers.
# number1 = int(input("enter number 1 :"))
# number2 = int(input("enter number 2 :"))
# number3 = int(input("enter number 3 :"))
# number4 = int(input("enter number 4 :"))

# if number1 > number2:
#     if number1 > number3:
#         if number1 > number4:
#             print("number 1 is big")
#         else:
#             print("number 4 is big")
#     else:
#         if number3 > number4:
#             print("number 3 is big")   
#         else:
#             print("number 4 is big")
# else:
#     if number2 > number3:
#         if number2 > number4:
#             print("number 2 is big")
#         else:
#             print("number 4 is big")
#     else:
#         if number3 > number4:
#             print("number 3 is big")
#         else:
#             print("number 4 is big")


# # Check if a triangle is valid based on its angles.
# angle1 = int(input("enter angle1:"))
# angle2 = int(input("enter angle2:"))
# angle3 = int(input("enter angle3:"))

# if angle1 + angle2 + angle3 == 180:
#     print("valid angle")
# else:
#     print("invalid")

# # Find the largest among three numbers using nested if.
# number1 = int(input("enter number 1 :"))
# number2 = int(input("enter number 2 :"))
# number3 = int(input("enter number 3 :"))
# if number1 > number2 :
#     if number1 > number3:
#         print("number1 is big")
#     else:
#         print("number3 is big")
# else:
#     if number2 > number3:
#         print("number2 is big")
#     else:
#         print("number3 is big")


# # Check if a number is divisible by 2, 3, and 5.
# number = int(input("enter the number:"))
# if number % 2 == 0 and number % 3 == 0 and number % 5 == 0:
#     print("number is divisible by all")
# else:
#     print("number is not divisible")

    
# # Check whether a person can apply for a driving license (age + ID available).
# age = int(input("enter the age :"))
# ID = input("enter ID:")
# if age >= 18:
#     if ID == "yes":
#         print("eligible for driving license")
#     else:
#         print("not eligible(ID required)")
# else:
#     print("age required")

# # Check admission eligibility based on marks and age.
# marks = int(input("enter marks :"))
# age = int(input("enter age :"))

# if marks >= 35:
#      if age >= 18:
#         print("Admission approved")

#      else:
#         print("under age")

# else:
#     print("Marks are required")

# # Check whether a person can enter a movie based on age.
# age = int(input("enter the age:"))
# if age >= 18:
#     print("person can enter")
# elif age <= 13:
#     print("allow only kids")
# elif age >= 13 and age <= 17:
#     print("allow PG-13 movie")
# else:
#     print("person cannot enter in movie")

# # Check whether a number is a palindrome (using conditions).
# number = input("enter number :")
# reverse_number = number[::-1]

# if number == reverse_number :
#     print("palindrome")
# else:
#     print("not palindrome")

# # Check whether a year is a century leap year.
# year = int(input("enter the yesr:"))

# if year%100 == 0:
#     if year%400 == 0:
#        print("century leap year")
#     else:
#         print("not leao year")
# else:
#     print("not a century leap year")

# # Determine the season based on the month number.
# month = int(input("enter the month :"))
# if month == 12 or month == 1 or month == 2:
#     print("winter")
# elif month == 3 or month == 4 or month == 5:
#     print("summer")
# elif month == 6 or month == 7 or month == 8:
#     print("Monsoon")
# else:
#     print("Autumn")

# # Check whether a password is strong (length, uppercase, lowercase, digit).
# password = input("enter password :")
# upper = False
# lower = False
# digit = False
# for ch in password:
#     if ch.isupper():
#         upper = True
#     if ch.islower():
#         lower = True
#     if ch.isdigit():
#         digit = True
# if len(password) >= 6 and upper and lower and digit:
#     print("password is strong")
# else:
#     print("please enter correct password")

# # Check whether three sides form an equilateral, isosceles, or scalene triangle.
# side1 = int(input("enter the side1 :"))
# side2 = int(input("enter the side2 :"))
# side3 = int(input("enter the side3 :"))
# if side1 + side2 > side3 and side1 + side3 > side2 and side2 + side3 > side1:
#     if side1 == side2 == side3 :
#         print("Equilateral")
#     elif side1 == side2 or side1 == side3 or side2 == side3:
#         print("isosceles")
#     else:
#         print("triangle")
# else:
#     print("invalid triangle")

# # Check whether a point lies in the first, second, third, or fourth quadrant.
# x = int(input("enter x:"))
# y = int(input("enter y:"))

# if x > 0 and y > 0:
#     print("first quadrant")
# elif x < 0 and y > 0:
#     print("second quadrant")
# elif x < 0 and y < 0:
#     print("third quadrant")
# elif x > 0 and y < 0:
#     print("fourth quadrant")
# elif x == 0 and y != 0:
#     print("on the y axis")
# elif x != 0 and y == 0:
#     print("on the x axis")
# else:
#     print("origin")

# # Calculate BMI and display the health category.
# weight = int(input("enter the weight:"))
# Height = float(input("enter the height:"))
# BMI = weight / (Height * Height)
# print("BMI is:", BMI)

# if BMI < 18.5:
#     print("Underweight")
# elif BMI > 18.5 and BMI < 24.9:
#     print("Normal")
# elif BMI > 25 and BMI < 29.9:
#     print("Overnight")
# else:
#     print("Obese")

# # Determine the day of the week based on a number (1–7).
# number = int(input("enter the number:"))
# if number == 1:
#     print("first day of week")
# elif number == 2:
#     print("second day of week")
# elif number == 3:
#     print("third day of week")
# elif number == 4:
#     print("fourth day of week")
# elif number == 5:
#     print("fifth day of week")
# elif number == 6:
#     print("sixth day of week")
# elif number == 7:
#     print("seventh day of week")
# else:
#     print("Invalid day")

