# Level 1 — Basic
# Print numbers from 1 to 10 using a while loop.
# i = 1
# while i <= 10:
#     print(i)
#     i += 1

# Print numbers from 10 to 1 using a while loop.
# i = 10
# while i >= 1:
#     print(i)
#     i -= 1

# Print all even numbers from 1 to 20.
# i = 1
# while i <= 20:
#   if i % 2 == 0:
#     print(i)
#   i += 1

# Print all odd numbers from 1 to 20.
# i = 1
# while i <= 20:
#   if i % 2 != 0:
#     print(i)
#   i += 1

# Print the multiplication table of 5.
# i = 1
# while i <= 10:
#     print(5 * i)
#     i += 1 

# Level 2 — Logic
# Find the sum of numbers from 1 to 10.
# i = 1
# sum = 0
# while i <= 10:
#     sum = sum + i
#     i += 1
# print(sum)

# Find the sum of all even numbers from 1 to 20.
# i = 1
# sum = 0
# while i <= 20:
#     if i % 2 == 0: 
#       sum = sum + i
#     i += 1
# print(sum)

# Take a number from the user and print its multiplication table.
# num = int(input("Enter a number: "))

# i = 1
# while i <= 10:
#     print(num, "x", i, "=", num * i)
#     i += 1

# Take a number from the user and count how many digits it has.
# Example: 12345 → 5 digits
# number = int(input("enter the number :"))
# count = 0
# while number > 0:
#     number = number // 10
#     count += 1
# print(count)

# armstrong number
# n = int(input("enter the number :"))
# original = n
# sum = 0
# while n > 0:
#     digit = n % 10
#     sum = sum + digit ** 3
#     n = n//10
# if original == sum:
#     print("armstrong number")
# else:
#     print("not armstrong number")

# Level 1 — Easy

# Q1. Count Digits
# while loop નો ઉપયોગ કરીને number માં કેટલા digits છે તે count કરો.
# number = int(input("enter the number:"))
# count = 0
# while number > 0:
#     number = number // 10
#     count = count+1
# print("total digits:",count )

# Q2. Sum of Digits
# Number ના બધા digits નો sum શોધો.
# number = int(input("enter the number:"))
# sum = 0
# while number > 0:
#     digit = number%10
#     sum = sum + digit
#     number = number // 10
# print(sum)







