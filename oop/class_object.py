# Basic Questions
# Create a class Student and create one object of it.
# class student:
#     pass
# s1 = student()
# print(s1)

# Create a class Person with a name variable and print the name using an object.
# class person:
#     name = "jeni"
# s1 = person()
# print(s1.name)

# Create a class Car with brand and color variables. Create an object and print both values.
# class Car:
#     brand = "BMW"
#     color = "white"
# s1 = Car()
# print(s1.brand)
# print(s1.color)

# Create a class Student with name and age. Create an object and display both values.
# class Student:
#     name = "jeni"
#     age = 21
# s1 = Student()
# print(s1.name)
# print(s1.age)

# Create a class Employee with name and salary. Create an object and print the employee details.
# class Employee:
#     name = "khush"
#     salary = 25000
# s1 = Employee()
# print(s1.name)
# print(s1.salary)

# Constructor Basic Questions
# Create a class Student with a constructor that accepts name and age, then display them.
# class Student:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
# s1 = Student("Jeni", 20)
# print(s1.name)
# print(s1.age)

# Create a class Car with a constructor that accepts brand and price. Create an object and display
#  the details.
# class Car:
#     def __init__(self, brand, price):
#         self.brand = brand
#         self.price = price
# s1 = Car("BMW",25000)
# print(s1.brand)
# print(s1.price)
        
# Create a class Rectangle with length and width. Use a constructor and calculate the area.
# class Rectangle:
#     def __init__(self, lenght, width):
#         self.lenght = lenght
#         self.width = width

#     def area(self):
#         return self.lenght * self.width
# s1 = Rectangle(52.2, 34)
# print("Area = ", s1.area())

# Create a class Circle with radius. Use a constructor and calculate the area of the circle.
# class Circle:
#     def __init__(self, radius):
#         self.radius = radius

#     def area(self):
#         return 3.14 * self.radius * self.radius
# s1 = Circle(5)
# print("radius=", s1.radius)
# print("Area=", s1.area())

# Create a class Calculator with two numbers and create methods for addition and subtraction.
# class Calculator:
#     def __init__(self, number1, number2):
#         self.number1 = number1
#         self.number2 = number2

#     def addition(self):
#         return self.number1 + self.number2

#     def subtraction(self):
#         return self.number1 - self.number2
    
# s1 = Calculator(45, 45)
# print("number1 =", s1.number1)
# print("number2 =", s1.number2)
# print("addition =", s1.addition())

# s2 = Calculator(45, 35)
# print("number1 =", s2.number1)
# print("number2 =", s2.number2)
# print("subtraction =", s2.subtraction())

# Constructor Practice Questions
# Create a Student class with a constructor that takes name and age. Display both values.
# class Student:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
# s1 = Student("priya", 23)
# print(s1.name)
# print(s1.age)        

# Create a Car class with a constructor that takes brand and price. Display the car details.
# class Car:
#     def __init__(self, brand, price):
#         self.brand = brand
#         self.price = price
# s1 = Car("farari", 2300000)
# print(s1.brand)
# print(s1.price)
      
# Create an Employee class with a constructor that takes name and salary. Display the employee details.
# class Employee:
#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary
# s1 = Employee("Tushar", 300000)
# print(s1.name)
# print(s1.salary)

# Create a Book class with a constructor that takes title and author. Display both values.
# class Book:
#     def __init__(self, title, author):
#         self.title = title
#         self.author = author
# s1 = Book("Rich dad poor dad", "robort kiyosaki")
# print(s1.title)
# print(s1.author)

# Create a Mobile class with a constructor that takes brand and price. Display the mobile details.
# class Mobile:
#     def __init__(self, brand,price):
#         self.brand = brand
#         self.price = price
# s1 = Mobile("iphone", 45000)
# print(s1.brand)
# print(s1.price)

# Create a Rectangle class with a constructor that takes length and width. Calculate and display 
# the area.
# class Rectangle:
#     def __init__(self, lenght, width):
#         self.lenght = lenght
#         self.width = width

#     def area(self):
#         return self.lenght * self.width
# s1 = Rectangle(52.2, 34)
# print("Area = ", s1.area())

# Create a Circle class with a constructor that takes radius. Calculate and display the area of the 
# circle.
# class Circle:
#     def __init__(self, radius):
#         self.radius = radius

#     def area(self):
#         return 3.14 * self.radius * self.radius
# s1 = Circle(5)
# print("radius=", s1.radius)
# print("Area=", s1.area())

# Create a Product class with a constructor that takes name, price, and quantity. Calculate and 
# display the total price.
# class Product:
#     def __init__(self,name, price, quantity):
#         self.name = name
#         self.price = price
#         self.quantity = quantity

#     def Total_price(self):
#         return self.price * self.quantity
# p1 = Product("Laptop", 25000, 4)
# print("Product Name:", p1.name)
# print("Price:", p1.price)
# print("Quantity:", p1.quantity)
# print("Total Price:", p1.Total_price())

# Create a BankAccount class with a constructor that takes account_holder and balance. 
# Display both values.
# class BankAccount:
#     def __init__(self, account_holder, balance):
#         self.account_holder = account_holder
#         self.balance = balance
# b1 = BankAccount("jeni", 50000)
# print(b1.account_holder)
# print(b1.balance)

# Create a Laptop class with a constructor that takes brand, ram, and price. Display all
#  laptop details.
# class Laptop:
#     def __init__(self, brand, ram, price):
#         self.brand = brand
#         self.ram = ram
#         self.price = price
# l1 = Laptop("Dell", "8GB", 50000)
# print("Brand:", l1.brand)
# print("RAM:", l1.ram)
# print("Price:", l1.price)