# list
# list = ["apple", "banana", "cherry", "apple", "banana"]
# print(list)

# append
# list = ["apple", "banana", "cherry", "apple", "banana"]
# list.append("orange")
# print(list)

# clear
# list = ["apple", "banana", "cherry", "apple", "banana"]
# list.clear()
# print(list)

# count
# list = ["apple", "banana", "cherry", "apple", "banana"]
# x = list.count("cherry")
# print(x)

# Extend
# list1 = [1, 2, 3]
# list2 = [4, 5, 6]

# list1.extend(list2)
# print(list1)

# index
# list1 = [1, 2, 3, 3, 5, 8, 9]
# x=list1.index(5)
# print(x)

# insert
# list1 = [1, 2, 3, 3, 5, 8, 9]
# list1.insert(4, 8)
# print(list1)

# reverse
# list1 = [1, 2, 3, 3, 5, 8, 9]
# list1.reverse()
# print(list1)

# sort
# list1 = [1, 2, 3, 3, 5, 8, 9]
# list1.sort()
# print(list1)

# 🟢 Easy — 1 to 5
# Q1. Append

# numbers = [10, 20, 30, 40]
# List ના અંતે 50 add કરો.
# numbers = [10, 20, 30, 40]
# numbers.append(50)
# print(numbers)

# Q2. Insert
# fruits = ["Apple", "Banana", "Mango"]
# "Orange" ને index 1 પર insert કરો.

# fruits = ["Apple", "Banana", "Mango"]
# fruits.insert(1, "orange")
# print(fruits)

# Q3. Extend
# a = [1, 2, 3]
# b = [4, 5, 6]
# b ના બધા elements a માં add કરો.

# a = [1, 2, 3]
# b = [4, 5, 6]
# a.extend(b)
# print(a)

# Q4. Remove
# names = ["Raj", "Amit", "Jay", "Amit", "Neha"]
# List માંથી "Amit" remove કરો.

# names = ["Raj", "Amit", "Jay", "Amit", "Neha"]
# names.remove("Amit")
# print(names)

# Q5. Pop
# numbers = [10, 20, 30, 40, 50]
# List માંથી last element pop() કરો અને updated list print કરો.

# numbers = [10, 20, 30, 40, 50]
# numbers.pop()
# print(numbers)

# 🟡 Medium — 6 to 10

# Q6. Count
# numbers = [2, 5, 2, 8, 2, 9, 5]
# 2 કેટલી વખત આવે છે તે શોધો.

# numbers = [2, 5, 2, 8, 2, 9, 5]
# a = numbers.count(2)
# print(a)

# Q7. Index
# fruits = ["Apple", "Mango", "Banana", "Orange"]
# "Banana" નો index શોધો.

# fruits = ["Apple", "Mango", "Banana", "Orange"]
# x = fruits.index("Banana")
# print(x)

# Q8. Sort
# numbers = [45, 12, 89, 23, 7, 56]
# Numbers ને ascending order માં sort કરો.

# numbers = [45, 12, 89, 23, 7, 56]
# numbers.sort()
# print(numbers)

# Q9. Reverse
# names = ["Raj", "Amit", "Neha", "Jay"]
# List ને reverse કરો.

# names = ["Raj", "Amit", "Neha", "Jay"]
# names.reverse()
# print(names)

# Q10. Clear
# data = [10, 20, 30, 40, 50]
# List ના બધા elements remove કરીને empty list બનાવો.

# data = [10, 20, 30, 40, 50]
# data.clear()
# print(data)

# 🔴 Advanced — 11 to 15

# Q11. Copy
# list1 = [10, 20, 30, 40]
# list1 ની copy બનાવીને list2 માં store કરો. પછી list2 માં 50 add કરો અને બંને lists print કરો.

# list1 = [10, 20, 30, 40]
# list2 = [10, 20, 30, 40]
# list2.append(50)
# print(list1)
# print(list2)

# Q12. Multiple Methods

# numbers = [10, 20, 30, 40, 50]
# 60 add કરો
# 25 ને index 2 પર insert કરો
# 40 remove કરો
# List ને descending order માં sort કરો

# numbers = [10, 20, 30, 40, 50]
# numbers.append(60)
# print(numbers)
# x = numbers.insert(2, 25)
# print(numbers)
# numbers.remove(40)
# print(numbers)
# numbers.sort(reverse=True)
# print(numbers)

# Q13. Duplicate Count

# numbers = [1, 2, 3, 2, 4, 2, 5, 3]
# 2 અને 3 કેટલી વખત આવે છે તે count() વડે શોધો.

# numbers = [1, 2, 3, 2, 4, 2, 5, 3]
# x = numbers.count(2)
# print(x)
# y = numbers.count(3)
# print(y)

# Q14. Find and Remove

# students = ["Rahul", "Amit", "Priya", "Jay", "Neha"]
# "Priya" નો index શોધો અને પછી તેને list માંથી remove કરો.

# students = ["Rahul", "Amit", "Priya", "Jay", "Neha"]

# x = students.index("Priya")
# print(x)
# students.remove("Priya")
# print(students)

# Q15. Combination Challenge 🔥

# numbers = [45, 12, 78, 12, 34, 90, 45, 23]

# 100 ને end માં add કરો
# 50 ને index 2 પર insert કરો
# 12 કેટલી વખત છે તે શોધો
# એક 45 remove કરો
# List ને ascending order માં sort કરો
# છેલ્લે list reverse કરો

# numbers = [45, 12, 78, 12, 34, 90, 45, 23]
# numbers.append(100)
# print(numbers)
# x = numbers.insert(2, 50)
# print(x)
# x = numbers.count(12)
# print(x)
# numbers.remove(45)
# print(numbers)
# numbers.sort()
# print(numbers)
# numbers.reverse()
# print(numbers)
