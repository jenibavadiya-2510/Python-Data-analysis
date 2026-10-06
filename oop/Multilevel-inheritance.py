# Multilevel-inhetitance
# class Animal:
#     def eat(self):
#         print("Animal can eat")


# class Dog(Animal):
#     def bark(self):
#         print("Dog can bark")


# class Puppy(Dog):
#     def play(self):
#         print("Puppy can play")

# p = Puppy()

# p.eat()
# p.bark()
# p.play()

# example 2
# class Grandfather:
#     def Grandfather(self):
#         print("grandfather")

# class Father(Grandfather):
#     def father(self):
#         print("father")

# class Son(Father):
#     def son(self):
#         print("son")

# s = Son()
# s.Grandfather()
# s.father()
# s.son()

# Create a LivingThing class, an Animal class that inherits from it, and a Dog class
#  that inherits from Animal.
# class LivingThing:
#     def live(self):
#         print("thing is living")

# class Animal(LivingThing):
#     def eat(self):
#         print("animal is eat")

# class Dog(Animal):
#     def bark(self):
#         print("dog can bark")

# d = Dog()
# d.live()
# d.eat()
# d.bark()

# Vehicle → Car → ElectricCar
# Write a Python program to demonstrate multilevel inheritance using Vehicle, Car, and ElectricCar 
# classes.

# class Vehicle:
#     def start(self):
#         print("vehicle can start")

# class Car(Vehicle):
#     def drive(self):
#         print("car can drive")

# class ElectricCar(Car):
#     def charge(self):
#         print("ElectricCar can be charged")

# E = ElectricCar()
# E.start()
# E.drive()
# E.charge()

# Company → Department → Employee
# Write a Python program to demonstrate multilevel inheritance using Company, Department, and 
# Employee classes.
# class Company:
#     def company_info():
#         print("company provides employment")

# class Department(Company):
#     def department_info():
#         print("Department manages employees")

# class Employee(Department):
#     def employee_info():
#         print("Employee performs work")

# e = Employee
# e.company_info()
# e.department_info()
# e.employee_info()

# extra question
# Q1. Person → Student → GraduateStudent
# Write a Python program to demonstrate multilevel inheritance using Person, Student, and 
# GraduateStudent classes. Create suitable methods and call all methods using the GraduateStudent 
# object.Methods: display_person(), study(), research()
# class Person:
#     def display_person(self):
#         print("display person info")

# class Student(Person):
#     def study(self):
#         print("student can study")

# class GraduateStudent(Student):
#     def research(self):
#         print("graduate student have a reserch")

# g = GraduateStudent()
# g.display_person()
# g.study()
# g.research()


# Q2. School → Teacher → MathTeacher
# Write a Python program using multilevel inheritance where School is inherited by Teacher, and 
# Teacher is inherited by MathTeacher. Create methods to display school, teacher, and subject 
# information.Methods: school_info(), teach(), solve_math()
# class School:
#     def school_info(self):
#         print("school has info")
# class Teacher(School):
#     def teach(self):
#         print("tracher has teach")
# class MathTeacher(Teacher):
#     def solve_math(self):
#         print("mathteacher solve maths")
# m = MathTeacher()
# m.school_info()
# m.teach()
# m.solve_math()

# Q3. Device → Computer → Laptop
# Write a Python program to demonstrate multilevel inheritance using Device, Computer, and Laptop. 
# Create suitable methods such as power_on(), process(), and carry().
# class Device:
#     def power_on(self):
#         print("Device is powered on")

# class Computer(Device):
#     def process(self):
#         print("Computer can process data")

# class Laptop(Computer):
#     def carry(self):
#         print("Laptop is easy to carry")

# l = Laptop()
# l.power_on()
# l.process()
# l.carry()

# Q4. Bank → Account → SavingsAccount
# Write a Python program using multilevel inheritance with Bank, Account, and SavingsAccount. 
# Create methods to display bank information, account information, and savings account information.
# Methods: bank_info(), account_info(), save_money()
# class Bank:
#     def bank_info(self):
#         print("bank has info")

# class Account(Bank):
#     def account_info(self):
#         print("account has information")

# class SavingsAccount(Account):
#     def save_money(self):
#         print("savingaccount use save money")

# s = SavingsAccount()
# s.bank_info()
# s.account_info()
# s.save_money()

# Q5. LivingThing → Animal → Cat
# Write a Python program to demonstrate multilevel inheritance using LivingThing, Animal, and Cat. 
# Create suitable methods and call all methods using a Cat object.
# Methods: breathe(), eat(), meow()
# class LivingThing:
#     def live(self):
#         print("thing is living")

# class Animal(LivingThing):
#     def eat(self):
#         print("animal is eat")

# class Cat(Animal):
#     def bark(self):
#         print("cat can meow")

# c = Cat()
# c.live()
# c.eat()
# c.cat()

# Q6. Food → Fruit → Mango
# Write a Python program using multilevel inheritance with Food, Fruit, and Mango. Create methods
#  to display food, fruit, and mango information.
# Methods: food_info(), fruit_info(), taste()
# class Food:
#     def food_info(self):
#         print("food has info")
# class Fruit(Food):
#     def fruit_info(self):
#         print("fruit has info")
# class Mango(Fruit):
#     def taste(self):
#         print("mango has taste")

# m = Mango()
# m.food_info()
# m.fruit_info()
# m.taste()

# Q7. Employee → Manager → GeneralManager
# Write a Python program to demonstrate multilevel inheritance using Employee, Manager, and GeneralManager. Create suitable methods to display information at each level.
# Methods: employee_info(), manage(), make_decision()
# class Employee:
#     def employee_info(self):
#         print("employee has info")
# class Manager(Employee):
#     def manage(self):
#         print("Manager has manage meetings")
# class GeneralManager(Manager):
#     def make_decision(self):
#         print("general manager can make decision")
# g = GeneralManager()
# g.employee_info()
# g.manage()
# g.make_decision()

# Q8. Transport → Bus → SchoolBus
# Write a Python program using multilevel inheritance where Transport is inherited by Bus, and Bus is inherited by SchoolBus. Create suitable methods and call all methods using a SchoolBus object.
# Methods: move(), carry_passengers(), carry_students()
# class Transport:
#     def move(self):
#         print("Transport can move")
# class Bus(Transport):
#     def carry_passengers(self):
#         print("Bus can carry passengers")
# class SchoolBus(Bus):
#     def carry_students(self):
#         print("School bus can carry students")
# s = SchoolBus()
# s.move()
# s.carry_passengers()
# s.carry_students()

# Q9. Person → Employee → Developer
# Write a Python program to demonstrate multilevel inheritance using Person, Employee, and Developer.
#  Create methods to display personal, employee, and developer information.
# Methods: person_info(), work(), write_code()
# class Person:
#     def person_info(self):
#         print("Person has personal information")
# class Employee(Person):
#     def work(self):
#         print("Employee can work")
# class Developer(Employee):
#     def write_code(self):
#         print("Developer can write code")
# d = Developer()
# d.person_info()
# d.work()
# d.write_code()

# Q10. University → College → Student
# Write a Python program using multilevel inheritance with University, College, and Student. 
# Create suitable methods and access all methods through the Student object.
# Methods: university_info(), college_info(), study()

# class University:
#     def university_info(self):
#         print("university has personal information")
# class College(University):
#     def college_info(self):
#         print("college has personal information")
# class Student(College):
#     def study(self):
#         print("student can study")
# s = Student()
# s.university_info()
# s.college_info()
# s.study()