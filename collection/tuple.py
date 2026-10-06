# tuple
# tup = ("apple", "banana", "cherry")
# print(tup)

# access tuple
# tup = ("apple", "banana", "cherry")
# print(tup[1])

# join
# tup1 = ("apple", "banana", "cherry")
# tup2 = ("mango", "grapes")
# tup3 = tup1 + tup2
# print(tup3)

# count
# tup1 = ("apple", "banana", "cherry", "banana")
# x = tup1.count("banana")
# print(x)

# index
# tup1 = ("apple", "banana", "cherry")
# x = tup1.index("apple")
# print(x)

# 🟢 LEVEL 1 — Basic
# Q1 — Access
# fruits = ("apple", "banana", "mango", "orange")
# "banana" print કરો.

# fruits = ("apple", "banana", "mango", "orange")
# print(fruits[1])

# Q2 — Access
# numbers = (10, 20, 30, 40, 50)
# 40 print કરો.

# numbers = (10, 20, 30, 40, 50)
# print(numbers[3])

# Q3 — Access
# student = ("Jeni", 21, "Surat")
# "Surat" print કરો.

# student = ("Jeni", 21, "Surat")
# print(student[2])

# Q4 — Join / Concatenation
# A = ("apple", "banana")
# B = ("mango", "orange")
# બંને tuples ને join કરો.

# A = ("apple", "banana")
# B = ("mango", "orange")
# join = A + B
# print(join)

# Q5 — Count
# numbers = (10, 20, 10, 30, 10, 40)
# 10 કેટલી વખત આવે છે તે શોધો.

# numbers = (10, 20, 10, 30, 10, 40)
# x = numbers.count(10)
# print(x)

# Q6 — Count
# fruits = ("apple", "banana", "apple", "mango", "apple")
# "apple" કેટલી વખત આવે છે તે શોધો.

# fruits = ("apple", "banana", "apple", "mango", "apple")
# x = fruits.count("apple")
# print(x)

# Q7 — Index
# fruits = ("apple", "banana", "mango", "orange")
# "mango" નો index શોધો.

# fruits = ("apple", "banana", "mango", "orange")
# a = fruits.index("mango")
# print(a)

# Q8 — Index
# numbers = (10, 20, 30, 40, 50)
# 40 નો index શોધો.

# numbers = (10, 20, 30, 40, 50)
# a = numbers.index(40)
# print(a)

# 🟡 LEVEL 2 — Easy
# Q9 — Access
# colors = ("red", "blue", "green", "yellow", "black")
# "green" access કરીને print કરો.

# colors = ("red", "blue", "green", "yellow", "black")
# print(colors[2])

# Q10 — Access
# student = ("Jeni", 21, "Python", "Surat")
# 21 access કરીને print કરો.

# student = ("Jeni", 21, "Python", "Surat")
# print(student[1])

# Q11 — Join
# A = (1, 2, 3)
# B = (4, 5, 6)
# A અને B ને join કરીને C tuple બનાવો.

# A = (1, 2, 3)
# B = (4, 5, 6)
# c = A + B
# print(c)

# Q12 — Join
# first = ("Python", "SQL")
# second = ("Excel", "Power BI")
# બંને tuples join કરો અને result print કરો.

# first = ("Python", "SQL")
# second = ("Excel", "Power BI")
# third = first + second
# print(third)

# Q13 — Count
# numbers = (5, 10, 5, 20, 5, 30, 5)
# 5 કેટલી વખત આવે છે?

# numbers = (5, 10, 5, 20, 5, 30, 5)
# x = numbers.count(5)
# print(x)

# Q14 — Count
# data = ("A", "B", "A", "C", "A", "D", "B")
# "A" અને "B" બંને કેટલી વખત આવે છે તે શોધો.

# data = ("A", "B", "A", "C", "A", "D", "B")
# x = data.count("A")
# y = data.count("B")

# print(x)
# print(y)

# Q15 — Final Challenge 🔥
# data = ("Python", "SQL", "Python", "Excel", "Power BI", "Python")
# આ ચાર operations કરો:

# "Python" access કરો.
# "Python" કેટલી વખત આવે છે તે શોધો.
# "Excel" નો index શોધો.
# આ tuple ને નીચેના tuple સાથે join કરો:
# new_data = ("Tableau", "Power BI")

# data = ("Python", "SQL", "Python", "Excel", "Power BI", "Python")
# print(data[0])
# x = data.count("python")
# print(x)
# y = data.index("Excel")
# print(y)
# new_data = ("Tableau", "PowerBI")
# tuple = data + new_data
# print(tuple)