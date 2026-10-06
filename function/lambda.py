
# add = lambda x,y:x+y
# print(add(2,3))

# square = lambda x:x*x
# print(square(5))

# check = lambda x: "even" if x%2==0 else "odd"
# print(check(5))
# print(check(8))

# Easy — Cube of a Number
# Write a lambda function to find the cube of a number.
# cube = lambda n: n**n
# print(cube(3))

# Q3. Easy — Addition
# Write a lambda function to add two numbers.
# add = lambda x,y:x+y
# print(add(2,3))

# Q4. Medium — Maximum of Two Numbers
# Write a lambda function that returns the maximum of two numbers.
# maximum = lambda a,b: a if a>b else b
# print(maximum(23,78))

# Q5. Medium — Even or Odd
# Write a lambda function to check whether a number is even or odd.
# check = lambda n: "Even" if n%2 == 0 else "odd"
# print(check(10))


# Q6. Medium — Positive or Negative
# Write a lambda function to check whether a number is positive, negative, or zero.
# check = lambda n: "positive" if n > 0 else "nagative" if n < 0 else "zero"
# print(check(5))
# print(check(-5))
# print(check(0))

# Q7. Hard — Maximum of Three Numbers
# Write a lambda function to find the maximum among three numbers.
# maximum = lambda a,b,c: a if a>b and a>c else b if b>c else c
# print(maximum(10, 25, 13))

# Q8. Hard — Calculate Simple Interest
# Write a lambda function to calculate simple interest using:
# SI = (P × R × T) / 100

# Write a lambda function to find the smaller of two numbers.
# number = lambda a,b: "a" if a>b else "b"
# print(number(34, 90)) 

# Write a lambda function to convert Celsius into Fahrenheit.
# celsius = lambda c:(c*9/5) + 32
# print(celsius(4))

# Sort the following numbers using lambda:
# numbers = [9, 2, 7, 1, 5]
# numbers.sort(key=lambda x:x)
# print(numbers)

# Sort the following words according to their length:
# words = ["cat", "elephant", "dog", "tiger"]
# words = ["cat", "elephant", "dog", "tiger"]
# words.sort(key=len)
# print(words)

# Use filter() with lambda to find all even numbers:
# numbers = [11, 24, 35, 42, 56, 67, 80]
# numbers = [11, 24, 35, 42, 56, 67, 80]
# result = list(filter(lambda x:x%2 == 0,numbers))
# print(result)

# Use filter() to find all positive numbers:
# numbers = [-10, 5, -3, 8, -1, 12]
# numbers = [-10, 5, -3, 8, -1, 12]
# result = list(filter(lambda x: x>0, numbers ))
# print(result)

# 🟡 Medium Level — map()

# Use map() and lambda to find the square of every number:
# numbers = [2, 4, 6, 8, 10]
# numbers = [2, 4, 6, 8, 10]
# square = list(map(lambda n: n*n, numbers))
# print(square)

# Use map() to convert all numbers into strings:
# numbers = [10, 20, 30, 40]
# numbers = [10, 20, 30, 40]
# strings = list(map(lambda x: str(x), numbers))
# print(strings)

# Use map() and lambda to convert all words into uppercase:
# words = ["python", "sql", "powerbi", "excel"]
# words = ["python", "sql", "powerbi", "excel"]
# upper = list(map(lambda x:x.upper(), words))
# print(upper)

# Use map() and lambda to find the length of every word:
# words = ["data", "python", "sql", "analysis"]
# words = ["data", "python", "sql", "analysis"]
# words.sort(key=len)
# print(words)

# Given two lists, multiply corresponding elements using map():
# A = [2, 3, 4, 5]
# B = [10, 20, 30, 40]
# A = [2, 3, 4, 5]
# B = [10, 20, 30, 40]
# result = list(map(lambda x,y:x*y,A,B))
# print(result)

# 🟠 Medium Level — filter()
# Find all numbers greater than 50:
# numbers = [20, 75, 45, 90, 30, 65]
# numbers = [20, 75, 45, 90, 30, 65]
# result = list(filter(lambda x:x>50, numbers))
# print(result)

# Find all odd numbers:
# numbers = [12, 15, 22, 31, 40, 47, 58]
# numbers = [12, 15, 22, 31, 40, 47, 58]
# result = list(filter(lambda x:x%2!=0, numbers))
# print(result)

# Find all names that start with "A":
# names = ["Amit", "Raj", "Ankit", "John", "Ajay"]
# names = ["Amit", "Raj", "Ankit", "John", "Ajay"]
# result = list(filter(lambda x:x.startswith("A"),names))
# print(result)

# Remove all empty strings from the list:
# words = ["python", "", "sql", "", "data", "powerbi"]
# words = ["python", "", "sql", "", "data", "powerbi"]
# result = list(filter(lambda x:x !="",words))
# print(result)

# Find all words having 5 or more characters:
# words = ["ai", "python", "data", "machine", "sql", "science"]
# words = ["ai", "python", "data", "machine", "sql", "science"]
# result = list(filter(lambda word: len(word) >= 5,words))
# print(result)

# Find all numbers divisible by both 3 and 5:
# numbers = [10, 15, 20, 30, 45, 50, 60]
# numbers = [10, 15, 20, 30, 45, 50, 60]
# result = list(filter(lambda x:x%3==0 and x%5==0,numbers))
# print(result)

# 🔴 Advanced — Dictionary + Lambda
# Sort students according to their marks:
# students = [
#     {"name": "A", "marks": 85},
#     {"name": "B", "marks": 95},
#     {"name": "C", "marks": 75}
# ]
# students = [
#     {"name": "A", "marks": 85},
#     {"name": "B", "marks": 95},
#     {"name": "C", "marks": 75}
# ]
# students.sort(key=lambda x:x["marks"])
# print(students)

# Sort employees according to their salary:
# employees = [
#     {"name": "Amit", "salary": 40000},
#     {"name": "Raj", "salary": 70000},
#     {"name": "John", "salary": 60000}
# ]
# employees.sort(key=lambda x:x["salary"])
# print(employees)


# Use filter() to find products whose price is greater than 1000:
# products = [
#     {"name": "Laptop", "price": 50000},
#     {"name": "Mouse", "price": 500},
#     {"name": "Phone", "price": 20000}
# ]
# result = list(filter(lambda x:x["price"]>1000,products))
# print(result)


# Use map() to add "pass" or "fail" based on marks. Passing marks = 50.
# students = [
#     {"name": "Amit", "marks": 35},
#     {"name": "Raj", "marks": 80},
#     {"name": "John", "marks": 45}
# ]
# result = list(map(lambda x: {
#      "name": x["name"],
#     "marks": x["marks"],
#     "result" : "pass" if x["marks"]>=50 else "fail"
# },students))
# print(result)

# Use filter() to find all palindrome words:
# words = ["madam", "python", "level", "data", "radar"]
# words = ["madam", "python", "level", "data", "radar"]
# result = list(filter(lambda x: x == x[::-1], words))
# print(result)

# Find the common elements between two lists using filter():
# A = [10, 20, 30, 40, 50]
# B = [30, 40, 50, 60, 70]
# result = list(filter(lambda x:x in A,B))
# print(result)

# Use map() and filter() together to count the number of vowels in each word:
# words = ["python", "java", "ai", "science"]
# result = list(map(lambda word: len(list(filter(lambda x: x in "aeiou", word))), words))
# print(result)
