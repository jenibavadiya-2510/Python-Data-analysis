# Single Inheritance — 20 Practice Questions
# Basic

# Create an Animal class with an eat() method. Create a Dog class that inherits from Animal and 
# add a bark() method.
# class Animal:
#     def eat(self):
#         print("Animal can eat")

# class Dog(Animal):
#     def bark(self):
#         print("Dog can bark")

# d1 = Dog()
# d1.eat()
# d1.bark()

# Create a Person class with a name variable. Create a Student class that inherits from Person and 
# display the name.
# class Person:
#     def name(self):
#         print("name of person")

# class Student(Person):
#     def name(self):
#         super().name()
#         print("name of student")

# n1 = Student()
# n1.name()

# Create a Vehicle class with a start() method. Create a Car class that inherits from Vehicle and 
# add a drive() method.
# class Vehicle:
#     def start(self):
#         print("vehicle can start")

# class Car(Vehicle):
#     def drive(self):
#         print("car can start")

# c1 = Car()
# c1.start()
# c1.drive()

# Create a Bird class with a fly() method. Create a Parrot class that inherits from Bird and add a 
# speak() method.
# class Bird:
#     def fly(self):
#         print("Bird can fly")

# class Parrot(Bird):
#     def speak(self):
#         print("parrot can speak")

# p1 = Parrot()
# p1.fly()
# p1.speak()

# Create a Shape class with a display() method. Create a Circle class that inherits from Shape and 
# add a radius variable.
# class Shape:
#     def display(self):
#         print("shape can display")

# class Circle(Shape):
#     def radius(self):
#         print("circle has radius")

# c1 = Circle()
# c1.display()
# c1.radius()

# Constructor + Inheritance
# Create a Person class with a constructor that takes name. Create a Student class that inherits
#  from Person and display the name.
# class Person:
#     def __init__(self,name):
#         self.name = name

# class Student(Person):
#     pass

# s1 = Student("jeni")
# print(s1.name)

# Create an Employee class with a constructor that takes name and salary. Create a Manager class 
# that inherits from Employee.
# class Employee:
#     def __init__(self,name,salary):
#         self.name = name
#         self.salary = salary

# class Manager(Employee):
#     pass

# m1 = Manager("jeni", 100000)
# print(m1.name)
# print(m1.salary)

# Create a Vehicle class with a constructor that takes brand. Create a Car class that inherits
#  from Vehicle and display the brand.
# class Vehicle:
#     def __init__(self,brand):
#         self.brand = brand

# class Car(Vehicle):
#     pass

# c1 = Car("suzuki")
# print(c1.brand)

# Create an Animal class with a constructor that takes name. Create a Dog class that inherits 
# from Animal and display the name.
# class Animal:
#     def __init__(self,name):
#         self.name = name

# class Dog(Animal):
#     pass

# d1 = Dog("puppy")
# print(d1.name)

# Create a Book class with a constructor that takes title. Create an EBook class that inherits 
# from Book and add file_size.
# class Book:
#     def __init__(self,title):
#         self.title = title

# class EBook(Book):
#     def __init__(self, title,file_size):
#         super().__init__(title)
#         self.file_size = file_size

# b1 = EBook("python basics", "5 MB")
# print(b1.title)
# print(b1.file_size)

# Intermediate
# Create a Person class with a name and age. Create a Student class that inherits from Person and 
# add roll_no.
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age


# class Student(Person):
#     def __init__(self, name, age, roll_no):
#         super().__init__(name, age)
#         self.roll_no = roll_no

# s1 = Student("Jeni", 20, 101)

# print(s1.name)
# print(s1.age)
# print(s1.roll_no)

# Create an Employee class with name and salary. Create a Developer class that inherits from
#  Employee and add programming_language.
# class Employee:
#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary

# class Developer(Employee):
#     def __init__(self, name, salary, programming_language):
#         super().__init__(name, salary)
#         self.programming_language = programming_language

# d1 = Developer("jeni", 200000, "python")
# print(d1.name)
# print(d1.salary)
# print(d1.programming_language)

# Create a Person class with name. Create a Student class that inherits from Person and adds roll_no.
# class Person():
#     def __init__(self,name):
#         self.name = name
    
#     def show_name(self):
#         print("name is :",self.name)

# class Student(Person):
#     def __init__(self,name,roll_no):
#         super().__init__(name)
#         self.roll_no = roll_no

#     def display(self):
#         print("student name :",self.name)
#         print("roll no is :",self.roll_no)

# s1 = Student("jensi",8)
# s1.show_name()
# s1.display()

# Create a Vehicle class with brand and price. Create a Car class that inherits from Vehicle and 
# add fuel_type.
# class Vehicle:
#     def __init__(self, brand, price):
#         self.brand = brand
#         self.price = price

#     def show_details(self):
#         print("brand is:", self.brand)
#         print("price is:", self.price)

# class Car(Vehicle):
#     def __init__(self, brand, price, fuel_type):
#         super().__init__(brand, price)
#         self.fuel_type = fuel_type

#     def display(self):
#         print("fuel type is:", self.fuel_type)

# c1 = Car("suzuki", 75000, "petrol")
# c1.show_details()
# c1.display()

# Create an Animal class with name and age. Create a Dog class that inherits from Animal and add
#  breed.
# class Animal:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age


# class Dog(Animal):
#     def __init__(self, name, age, breed):
#         super().__init__(name, age)
#         self.breed = breed


# d1 = Dog("Tommy", 3, "Labrador")

# print(d1.name)
# print(d1.age)
# print(d1.breed)

# Create a Product class with name and price. Create an ElectronicProduct class that inherits 
# from Product and add warranty.
# class Product:
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price

#     def show_details(self):
#         print("name is:", self.name)
#         print("price is:", self.price)

# class ElectronicProduct(Product):
#     def __init__(self, name, price, warranty):
#         super().__init__(name, price)
#         self.warranty = warranty

#     def display(self):
#         print("warranty is:", self.warranty)

# e1 = ElectronicProduct("TV", 65000, "2 year")
# e1.show_details()
# e1.display()

# Method-Based
# Create a Calculator class with an add() method. Create a ScientificCalculator class that inherits 
# from Calculator and add a square() method.
# class Calculator:
#     def add(self, a, b):
#         print("Addition =", a+b)

# class ScientificCalculator(Calculator):
#     def square(self, n):
#         print("square =", n*n)

# s1 = ScientificCalculator()
# s1.add(10, 20)
# s1.square(5)

# Create a BankAccount class with deposit() method. Create a SavingsAccount class that inherits 
# from BankAccount and add an interest() method.
# class BankAccount:
#     def __init__(self, deposit, interest):
#         self.deposit = deposit
#         self.interest = interest

#     def show_details(self):
#         print("Deposit is:", self.deposit)


# class SavingsAccount(BankAccount):
#     def display(self):
#         print("Interest is:", self.interest)


# deposit = int(input("Enter the deposit: "))
# rate = int(input("Enter the interest: "))

# s1 = SavingsAccount(deposit, rate)

# s1.show_details()
# s1.display()

# Create a Shape class with an area() method. Create a Rectangle class that inherits from Shape and 
# calculate the rectangle's area.
# class Shape:
#     def area(self):
#         print("Shape has an area")

# class Rectangle(Shape):
#     def calculate_area(self, length, width):
#         print("Area =", length * width)

# r1 = Rectangle()

# r1.area()
# r1.calculate_area(10, 5)

# Create a Person class with a display() method. Create a Student class that inherits from Person 
# and add a study() method.
# class Person:
#     def display(self):
#         print("display person details")

# class Student(Person):
#     def study(self):
#         print("student can study")

# s = Student()
# s.display()
# s.study()

# Create a Vehicle class with start() and stop() methods. Create a Bike class that inherits from 
# Vehicle and add a ride() method.
# class Vehicle:
#     def start(self):
#         print("vehicle can start")

#     def stop(self):
#         print("vehicle can stop")

# class Bike(Vehicle):
#     def ride(self):
#         print("bike can ride")

# b = Bike()
# b.start()
# b.stop()
# b.ride()