# Find the sum of numbers from 1 to 100.
# sum = 0
# for i in range(1, 101):
#     sum = sum+i
# print(sum)

# Q1. 1 થી 10 સુધીના numbers print કરો.
# for i in range(1, 11):
#     print(i)

#Q2. 1 થી 20 સુધીના even numbers print કરો.
# for i in range(1, 21):
#     if i % 2 == 0:
#         print(i)

# Q3. આ list માંથી દરેક number print કરો
# marks = [45, 67, 89, 32, 76]
# for mark in marks:
#     print(mark)

# Q4. 1 થી 10 સુધીના numbers નો sum find કરો.
# sum = 0
# for i in range (1, 11):
#     sum = sum+i
# print(sum)

# For Loop – 20 Practice Questions

# Print numbers from 10 to 1.
# for i in range(10, 0 , -1):
#     print(i)

# Print all even numbers from 1 to 20.
# for i in range(1, 21):
#     if i % 2 == 0:
#         print(i)

# Print all odd numbers from 1 to 20.
# for i in range(1, 21):
#     if i % 2 != 0:
#         print(i)

# Find the sum of numbers from 1 to 10.
# sum = 0
# for i in range(1, 11):
#     sum = sum+i
# print(sum)

# Find the sum of all even numbers from 1 to 50.
# sum = 0
# for i in range(1, 51):
#     if i % 2 == 0: 
#      sum = sum+i
# print(sum)

# Print each element from this list:
# marks = [45, 67, 89, 32, 76]

# marks = [45, 67, 89, 32, 76]
# for mark in marks:
#     print(mark)

# Find the highest number from:
# numbers = [25, 78, 12, 90, 45, 67]

# numbers = [25, 78, 12, 90, 45, 67]
# for num in numbers:
#     print(num)

# Find the lowest number from:
# numbers = [25, 78, 12, 90, 45, 67]
# numbers = [25, 78, 12, 90, 45, 67]

# lowest = numbers[0]

# for num in numbers:
#     if num < lowest:
#         lowest = num
# print(lowest)

# Count how many numbers are greater than 50:
# numbers = [25, 67, 45, 89, 32, 76, 50]
# count = 0
# for num in numbers:
#     if num > 50:
#          count = count + 1
# print(count)

# Print only the positive numbers:
# numbers = [-5, 10, -2, 8, -7, 15]
# for num in numbers:
#     if num > 0:
#         print(num)

# Print the square of each number from 1 to 10.
# for i in range(1, 11):
#     i = i*i
#     print(i)

# Print the multiplication table of 5.
# for i in range(1, 10):
#     i = 5 * i
#     print(i)

# Print the multiplication tables from 1 to 5.
# for i in range(1, 6):
#     for j in range(1, 11):
#         print(i, "x", j, "=", i * j)
#     print()

# Count the number of even numbers in:
# numbers = [12, 7, 9, 20, 34, 15, 18]
# for num in numbers:
#     if num % 2 == 0:
#      print(num)

# Find the total sales:
# sales = [1200, 2500, 1800, 3200, 1500]
# sum = 0
# for num in sales:
#     sum = sum+num
# print(sum)

# Print names whose length is greater than 5:
# names = ["Jeni", "Rahul", "Priya", "Amit", "Krishna"]
# for name in names:
#     if len(name) > 5:
#         print(name)

# Count how many times "Python" appears:
# subjects = ["SQL", "Python", "Excel", "Python", "Power BI", "Python"]

# count = 0
# for subject in subjects:
#     if subject == "Python":
#         count = count + 1
# print(count)

# Find the second-highest number from:
# numbers = [45, 89, 23, 76, 95, 67, 89]
# highest = 45

# for i in numbers:
#     if i > highest:
#         highest = i

#         print("second highest number :",highest)
#         i = i+1
#         break

#Find the factorial of a number.
# number = int(input("enter the number : "))
# fact = 1
# for i in range(1, number+1):
#      fact = fact*i
# print(fact)

# factorial number
# n = 5
# fact = 1
# for i in range(1, n+1):
#     fact = fact * i
# print(fact)

# fibonacci series
# n = 10
# a = 0
# b = 1
# for i in range(n):
#     print(a)
#     c = a+b
#     a = b
#     b = c

#palindrome number
# n = int(input("enter the number :"))
# original = n
# reverse = 0
# while n>0:
#     digit = n % 10
#     reverse = reverse * 10 + digit
#     n = n//10
# if original == reverse:
#     print("palindrome")
# else:
#     print("not palindrome")

