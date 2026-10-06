# Basic Questions
# Q1. Create an Animal class with an eat() method. Create Dog and Cat classes that inherit from 
# Animal. Add bark() and meow() methods.
# class Animal:
#     def eat(self):
#         print("Animal can eat")

# class Dog(Animal):
#     def bark(self):
#         print("Dog can bark")

# class Cat(Animal):
#     def meow(self):
#         print("Cat can meow")

# d = Dog()
# d.eat()
# d.bark()

# c = Cat()
# c.eat()
# c.meow()

# Q2. Create a Person class with a display() method. Create Student and Teacher classes that 
# inherit from Person. Add study() and teach() methods.
# class Person:
#     def display(self):
#         print("display person info")
# class Student(Person):
#     def study(self):
#         print("student has study")
# class Teacher(Person):
#     def teach(self):
#         print("teacher can teach")

# s = Student()
# s.display()
# s.study()

# t = Teacher()
# t.display()
# t.teach()

# Q3. Create a Vehicle class with a start() method. Create Car and Bike classes that inherit 
# from Vehicle. Add drive() and ride() methods.
# class Vehicle:
#     def start(self):
#         print("vehicle can start")
# class Car(Vehicle):
#     def drive(self):
#         print("car can drive")
# class Bike(Vehicle):
#     def ride(self):
#         print("bile can ride")
# c = Car()
# c.start()
# c.drive()

# b = Bike()
# b.start()
# b.ride()

# Q4. Create an Employee class with a work() method. Create Manager and Developer classes that 
# inherit from Employee. Add manage() and code() methods.
# class Employee:
#     def work(self):
#         print("employee have a work")
# class Manager(Employee):
#     def manage(self):
#         print("manager has manage work")
# class Developer(Employee):
#     def code(self):
#         print("Developer write code")
# m = Manager()
# m.work()
# m.manage()

# d = Developer()
# d.work()
# d.code()

# Q5. Create a Shape class with a display() method. Create Circle and Rectangle classes that 
# inherit from Shape. Add circle_area() and rectangle_area() methods.
# class Shape:
#     def display(self):
#         print("This is a shape")
# class Circle(Shape):
#     def circle_area(self):
#         radius = 5
#         area = 3.14 * radius * radius
#         print("Circle Area:", area)
# class Rectangle(Shape):
#     def rectangle_area(self):
#         length = 10
#         width = 5
#         area = length * width
#         print("Rectangle Area:", area)
# c = Circle()
# c.display()
# c.circle_area()

# r = Rectangle()
# r.display()
# r.rectangle_area()


# 🔹 5 Questions with __init__()

# Q1. Person → Student + Teacher
# Question:

# Create a Person class with name and age. Create Student and Teacher classes that inherit from Person.

# Person → __init__(name, age) અને show_person()
# Student → __init__(name, age, course) અને show_student()
# Teacher → __init__(name, age, subject) અને show_teacher()
# Use super() to initialize parent class attributes.
# Take input from the user for both Student and Teacher.
# Display all details.

# class Person:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age

#     def show_person(self):
#         print("name is:", self.name)
#         print("age is:",self.age)

# class Student(Person):
#     def __init__(self, name, age,course):
#         super().__init__(name, age)
#         self.course = course

#     def show_student(self):
#        print("course is:", self.course)

# class Teacher(Person):
#     def __init__(self, name, age,subject):
#         super().__init__(name, age)
#         self.subject = subject

#     def show_teacher(self):
#         print("subject is:",self.subject)

# name = input("enter your name:")
# age = int(input("enter the age:"))
# course = input("enter the course:")

# a = Student(name, age,course)
# a.show_person()
# a.show_student()

# print()

# name = input("enter your name :") 
# age = int(input("enter your age:"))
# subject = input("enter the subject:")

# a = Teacher(name,age,subject)
# a.show_person() 
# a.show_teacher() 

# Q2. Vehicle → Car + Bike
# Question:

# Create a Vehicle class with brand and price. Create Car and Bike classes
#  that inherit from Vehicle.

# Requirements:

# Vehicle class:

# __init__(brand, price)
# show_vehicle()

# Car class:

# __init__(brand, price, model)
# Use super()
# show_car()

# Bike class:

# __init__(brand, price, bike_type)
# Use super()
# show_bike()

# Take input from the user and display both Car and Bike details.

# class Vehicle:
#     def __init__(self,brand,price):
#         self.brand = brand
#         self.price = price
#     def show_vehicle(self):
#         print("brand is:",self.brand)
#         print("price is:",self.price)

# class Car(Vehicle):
#     def __init__(self, brand, price,model):
#         super().__init__(brand, price)
#         self.model = model
#     def show_car(self):
#         print("model is:",self.model)

# class Bike(Vehicle):
#     def __init__(self, brand, price, bike_type):
#         super().__init__(brand, price)
#         self.bike_type = bike_type
#     def show_bike(self):
#         print("bike type is:", self.bike_type)

# brand = input("enter car brand :")
# price = int(input("enter car price:"))
# model = input("enter car model:")

# c = Car(brand,price,model)
# c.show_vehicle()
# c.show_car()

# brand = input("enter the brand :")
# price = int(input("enter the price:"))
# bike_type = input("enter the bike type :")

# c = Bike(brand,price,bike_type)
# c.show_vehicle()
# c.show_bike()


# Q3. Account → SavingAccount + CurrentAccount
# Question:

# Create an Account class with account_holder and balance. Create SavingAccount and
#  CurrentAccount classes that inherit from Account.

# Requirements:

# Account class:
# __init__(account_holder, balance)
# show_account()

# SavingAccount class:
# __init__(account_holder, balance, interest_rate)
# Use super()
# show_saving()

# CurrentAccount class:
# __init__(account_holder, balance, overdraft_limit)
# Use super()
# show_current()

# Take user input for both accounts and display all details.

# class Account:
#     def __init__(self, account_holder, balance):
#         self.account_holder = account_holder
#         self.balance = balance
#     def show_account(self):
#         print("Account Holder:", self.account_holder)
#         print("Balance:", self.balance)


# class SavingAccount(Account):
#     def __init__(self, account_holder, balance, interest_rate):
#         super().__init__(account_holder, balance)
#         self.interest_rate = interest_rate
#     def show_saving(self):
#         print("Interest Rate:", self.interest_rate)


# class CurrentAccount(Account):
#     def __init__(self, account_holder, balance, overdraft_limit):
#         super().__init__(account_holder, balance)
#         self.overdraft_limit = overdraft_limit
#     def show_current(self):
#         print("Overdraft Limit:", self.overdraft_limit)

# # Saving Account
# account_holder = input("Enter saving account holder: ")
# balance = int(input("Enter balance: "))
# interest_rate = int(input("Enter interest rate: "))

# s = SavingAccount(account_holder, balance, interest_rate)

# s.show_account()
# s.show_saving()

# print()

# # Current Account
# account_holder = input("Enter current account holder: ")
# balance = int(input("Enter balance: "))
# overdraft_limit = int(input("Enter overdraft limit: "))

# c = CurrentAccount(account_holder, balance, overdraft_limit)

# c.show_account()
# c.show_current()

# Q4. Employee → Manager + Developer

# Create an Employee class with name and salary. Create Manager and Developer classes that 
# inherit from Employee.

# Requirements:

# Employee:

# __init__(name, salary)
# show_employee()

# Manager:

# __init__(name, salary, department)
# Use super()
# show_manager()

# Developer:

# __init__(name, salary, programming_language)
# Use super()
# show_developer()

# Take input from the user and display details of Manager and Developer.

# class Employee:
#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary
#     def show_employee(self):
#         print("name is:", self.name)
#         print("salary is:", self.salary)

# class Manager(Employee):
#     def __init__(self, name, salary, department):
#         super().__init__(name, salary)
#         self.department = department
#     def show_manager(self):
#         print("department is:", self.department)

# class Developer(Employee):
#     def __init__(self, name, salary, programming_language):
#         super().__init__(name, salary)
#         self.programming_language = programming_language
#     def show_developer(self):
#         print("programming_language is:", self.programming_language)

# name = input("enter the name:")
# salary = int(input("enter the salary:"))
# department = input("enter the department :")

# m = Manager(name,salary,department)
# m.show_employee()
# m.show_manager()

# print()

# name = input("enter the name:")
# salary = int(input("enter the salary:"))
# programming_language = input("enter the programming language:")

# d = Developer(name,salary,programming_language)
# d.show_employee()
# d.show_developer()


# Q5. Student → ScienceStudent + CommerceStudent

# Create a Student class with name and marks. Create ScienceStudent and CommerceStudent classes 
# that inherit from Student.

# Requirements:

# Student class:

# __init__(name, marks)
# show_student()

# ScienceStudent class:

# __init__(name, marks, science_subject)
# Use super()
# show_science()

# CommerceStudent class:

# __init__(name, marks, commerce_subject)
# Use super()
# show_commerce()

# Take input from the user for both students and display their details.

# class Student:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks
#     def show_student(self):
#         print("name is:", self.name)
#         print("marks is:",self.marks)

# class Sciencestudent(Student):
#     def __init__(self, name, marks,science_subject):
#         super().__init__(name, marks)
#         self.science_subject = science_subject
#     def show_science(self):
#         print("science subject is:", self.science_subject)

# class Commercestudent(Student):
#     def __init__(self, name, marks, commerce_subject):
#         super().__init__(name, marks)
#         self.commerce_subject = commerce_subject
#     def show_commerce(self):
#         print("commerce subject is:", self.commerce_subject)

# name = input("enter science student name:")
# marks = int(input("enter marks:"))
# science_subject = input("enter science subject:")

# s = Sciencestudent(name,marks,science_subject)
# s.show_student()
# s.show_science()

# print()

# name = input("enter commerce student name:")
# marks = int(input("enter marks:"))
# commerce_subject = input("enter commerce subject:")

# c = Commercestudent(name,marks,commerce_subject)
# c.show_student()
# c.show_commerce()