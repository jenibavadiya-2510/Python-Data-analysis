#Dictionaries

# dict = {
#     "name" : "jeni",
#     "age" : 21
# }
# print(dict)

# len
# dict = {
#     "name" : "jeni",
#     "age" : 21
# }
# print(len(dict))

# keys
# dict = {
#     "name" : "jeni",
#     "age" : 21
# }
# x = dict.keys()
# print(x)

# values
# dict = {
#     "name" : "jeni",
#     "age" : 21
# }
# x = dict.values()
# print(x)

# clear
# dict = {
#     "name" : "jeni",
#     "age" : 21
# }
# dict.clear()

# update
# dict = {
#     "name" : "jeni",
#     "age" : 21
# }
# dict.update({"marks" : 90})
# print(dict)

# LEVEL 1 — Very Easy
# Q1 — len()
# student = {
#      "name": "Jeni",
#      "age": 21
# }
# print(len(student))

# Dictionary માં કુલ કેટલા items છે તે print કરો.

# Q2 — keys()
# student = {
#     "name": "Jeni",
#     "age": 21,
#     "city": "Surat"
# }
# Dictionary ની બધી keys print કરો.

# student = {
#     "name": "Jeni",
#     "age": 21,
#     "city": "Surat"
# }
# a = student.keys()
# print(a)

# Q3 — values()
# student = {
#     "name": "Jeni",
#     "age": 21,
#     "city": "Surat"
# }
# Dictionary ના બધા values print કરો.

# student = {
#     "name": "Jeni",
#     "age": 21,
#     "city": "Surat"
# }
# x = student.values()
# print(x)

# Q4 — clear()
# student = {
#     "name": "Jeni",
#     "age": 21,
#     "city": "Surat"
# }
# Dictionary ના બધા items remove કરો અને પછી dictionary print કરો.

# student = {
#     "name" : "jeni",
#     "age" : 21,
#     "city" : "surat"
# }
# student.clear()

# Q5 — update()
# student = {
#     "name": "Jeni",
#     "age": 21
# }
# Dictionary માં આ item add કરો: city = Surat

# student = {
#     "name": "Jeni",
#     "age": 21
# }
# student.update({"city" : "surat"})
# print(student)

# 🟡 LEVEL 2 — Easy

# Q6 — len()
# employee = {
#     "name": "Rahul",
#     "age": 25,
#     "department": "IT",
#     "salary": 40000
# }
# Dictionary માં કુલ કેટલા items છે તે શોધો.

# employee = {
#     "name": "Rahul",
#     "age": 25,
#     "department": "IT",
#     "salary": 40000
# }
# print(len(employee))

# Q7 — keys()
# product = {
#     "name": "Laptop",
#     "price": 50000,
#     "brand": "Dell",
#     "stock": 10
# }
# માત્ર dictionary ની keys print કરો.

# product = {
#     "name": "Laptop",
#     "price": 50000,
#     "brand": "Dell",
#     "stock": 10
# }
# x = product.keys()
# print(x)

# Q8 — values()
# product = {
#     "name": "Laptop",
#     "price": 50000,
#     "brand": "Dell",
#     "stock": 10
# }
# માત્ર values print કરો.

# product = {
#     "name": "Laptop",
#     "price": 50000,
#     "brand": "Dell",
#     "stock": 10
# }
# x = product.values()
# print(x)

# Q9 — update()
# employee = {
#     "name": "Amit",
#     "age": 24
# }
# એક સાથે નીચેના બે items add કરો:
# department = "HR"
# city = "Ahmedabad"

# 👉 update() use કરો.

# employee = {
#     "name": "Amit",
#     "age": 24
# }
# employee.update({
#     "department" : "HR",
#     "city" : "Ahmedabad"})
# print(employee)

# Q10 — clear()
# cart = {
#     "product1": "Laptop",
#     "product2": "Mouse",
#     "product3": "Keyboard"
# }
# Customer આખી cart empty કરે છે.
# clear() use કરીને dictionary empty કરો.

# cart = {
#     "product1": "Laptop",
#     "product2": "Mouse",
#     "product3": "Keyboard"
# }
# cart.clear()
# print(cart)

# level 3 : hard

# Q16 — len() + update()
# student = {
#     "name": "Amit",
#     "age": 22
# }
# update() થી 3 નવા items add કરો અને પછી len() થી total items શોધો.

# student = {
#     "name": "Amit",
#     "age": 22
# }
# student.update({
#     "marks": 56,
#     "city":"surat",
#     "college_name":"ssasit"
# })
# print(student)
# print(len(student))

# Q17 — keys() + update()
# product = {
#     "name": "Laptop",
#     "price": 50000
# }
# update() થી brand અને stock add કરો.
# પછી keys() થી બધી keys print કરો.

# product = {
#     "name": "Laptop",
#     "price": 50000
# }
# product.update({
#     "brand":"DELL",
#     "stock":10000
# })
# j = product.keys()
# print(j)

# Q18 — values() + update()
# product = {
#     "name": "Laptop",
#     "price": 50000
# }

# update() થી:brand = "Dell",stock = 10
# add કરો.પછી values() થી બધા values print કરો.

# product = {
#     "name": "Laptop",
#     "price": 50000
# }
# product.update({
#     "brand":"DELL",
#     "stock":100
# })
# j = product.values()
# print(j)

# Q19 — All Methods 🔥
# company = {
#     "name": "ABC",
#     "city": "Surat"
# }

# આ બધું કરો:
# update() → employees = 100, industry = "IT" add કરો.
# len() → total items શોધો.
# keys() → બધા keys print કરો.
# values() → બધા values print કરો.

# company = {
#     "name": "ABC",
#     "city": "Surat"
# }
# company.update({
#     "employee":100,
#     "industry":"IT"
# })
# print(company)
# print(len(company))
# x = company.keys()
# print(x)
# y = company.values()
# print(y)


# Q20 — Final Challenge 🔥
# student = {
#     "name": "Jeni",
#     "age": 21
# }

# update() → city, course, marks add કરો.
# len() → total items print કરો.
# keys() → keys print કરો.
# values() → values print કરો.
# clear() → આખી dictionary empty કરો.
# Dictionary print કરો.

# student = {
#     "name": "Jeni",
#     "age": 21
# }
# student.update({
#     "city":"surat",
#     "course":"It",
#     "marks":56
# })
# print(student)
# print(len(student))
# x = student.keys()
# print(x)
# y = student.values()
# print(y)
# student.clear()