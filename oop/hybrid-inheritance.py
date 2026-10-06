# hybrid example
# class A:
#     def show_a(self):
#         print("Class A")

# class B(A):
#     def show_b(self):
#         print("Class B")

# class C(A):
#     def show_c(self):
#         print("Class C")

# class D(B, C):
#     def show_d(self):
#         print("Class D")

# d = D()

# d.show_a()
# d.show_b()
# d.show_c()
# d.show_d()

# Basic Questions
# Q1. Animal → Dog + Cat → Pet

# Create an Animal class with an eat() method. Create Dog and Cat classes that inherit from Animal.
#  Then create a Pet class that inherits from both Dog and Cat.

# Methods:
# Animal → eat()
# Dog → bark()
# Cat → meow()
# Pet → play()

# class Animal:
#     def eat(self):
#         print("animal can eat")
# class Dog(Animal):
#     def bark(self):
#         print("dog can bark")
# class Cat(Animal):
#     def meow(self):
#         print("cat can meow")
# class Pet(Dog, Cat):
#     def play(self):
#         print("pet can play")

# p = Pet()
# p.eat()
# p.bark()
# p.meow()
# p.play()

# Q2. Person → Student + Employee → WorkingStudent

# Create a Person class with a display() method. Create Student and Employee classes that inherit 
# from Person. Create WorkingStudent that inherits from both Student and Employee.

# Methods:

# Person → display()
# Student → study()
# Employee → work()
# WorkingStudent → manage_time()

# class Person:
#     def display(self):
#         print("display person info")
# class Student(Person):
#     def study(self):
#         print("student can study")
# class Employee(Person):
#     def work(self):
#         print("employee can work")
# class WorkingStudent(Student, Employee):
#     def manage_time(self):
#         print("working student manage time")
# w = WorkingStudent()
# w.display()
# w.study()
# w.work()
# w.manage_time()

# Q3. Vehicle → Car + Bike → SportsVehicle

# Create a Vehicle class with a start() method. Create Car and Bike classes that inherit from 
# Vehicle. Create SportsVehicle that inherits from both Car and Bike.

# Methods:

# Vehicle → start()
# Car → drive()
# Bike → ride()
# SportsVehicle → race()

# class Vehicle:
#     def start(self):
#         print("Vehicle can start")
# class Car(Vehicle):
#     def drive(self):
#         print("Car can drive")
# class Bike(Vehicle):
#     def ride(self):
#         print("Bike can ride")
# class SportsVehicle(Car, Bike):
#     def race(self):
#         print("Sports vehicle can race")
# s = SportsVehicle()

# s.start()
# s.drive()
# s.ride()
# s.race()

# Q4. Employee → Manager + Developer → TeamLead

# Create an Employee class with a work() method. Create Manager and Developer classes that inherit
#  from Employee. Create TeamLead that inherits from both Manager and Developer.

# Methods:

# Employee → work()
# Manager → manage()
# Developer → code()
# TeamLead → lead_team()

# class Employee:
#     def work(self):
#         print("Employee can work")
# class Manager(Employee):
#     def manage(self):
#         print("Manager can manage")
# class Developer(Employee):
#     def code(self):
#         print("Developer can code")
# class TeamLead(Manager, Developer):
#     def lead_team(self):
#         print("Team Lead can lead the team")
# t = TeamLead()

# t.work()
# t.manage()
# t.code()
# t.lead_team()

#Q5: Device → Computer + Phone → SmartDevice

# Create a Device class with a power_on() method. Create Computer and Phone classes that inherit 
# from Device. Create SmartDevice that inherits from both Computer and Phone.

# Methods:

# Device → power_on()
# Computer → process()
# Phone → call()
# SmartDevice → use_apps()

# class Device:
#     def power_on(self):
#         print("device is power on")
# class Computer(Device):
#     def process(self):
#         print("computer process work")
# class Phone(Device):
#     def call(self):
#         print("phone use for call")
# class SmartDevice(Computer, Phone):
#     def use_apps(self):
#         print("smart deivce use apps")
# s = SmartDevice()
# s.power_on()
# s.process()
# s.call()
# s.use_apps()

# Questions with __init__()

# Q6. Person → Student + Teacher → Professor

# Create a Person class with an __init__() method to initialize name.
# Create Student and Teacher classes that inherit from Person.
# Create Professor that inherits from both Student and Teacher.

# Attributes:

# Person → name # Student → course # Teacher → subject
# Professor → experience

# Methods:

# show_person()
# show_student()
# show_teacher()
# show_professor()

# Use: super().__init__().

# class Person:
#     def __init__(self, name):
#         self.name = name
#     def show_person(self):
#         print("Name:", self.name)

# class Student(Person):
#     def __init__(self, name, course):
#         Person.__init__(self, name)
#         self.course = course
#     def show_student(self):
#         print("Course:", self.course)

# class Teacher(Person):
#     def __init__(self, name, subject):
#         Person.__init__(self, name)
#         self.subject = subject
#     def show_teacher(self):
#         print("Subject:", self.subject)

# class Professor(Student, Teacher):
#     def __init__(self, name, course, subject, experience):
#         Student.__init__(self, name, course)
#         self.subject = subject
#         self.experience = experience
#     def show_professor(self):
#         print("Experience:", self.experience, "years")


# p = Professor("Jeni", "Python", "Programming", 5)

# p.show_person()
# p.show_student()
# p.show_teacher()
# p.show_professor()

# Q7. Vehicle → Car + Bike → SportsVehicle

# Create a Vehicle class with brand and price.
# Create Car and Bike classes that inherit from Vehicle.
# Create SportsVehicle that inherits from both Car and Bike.

# Attributes:

# Vehicle → brand, price
# Car → model
# Bike → bike_type
# SportsVehicle → speed

# Methods:

# show_vehicle()
# show_car()
# show_bike()
# show_sports()

# Use super() wherever required.

# class Vehicle:
#     def __init__(self,brand,price):
#        self.brand = brand
#        self.price = price
#     def show_vehicle(self):
#         print("brand is:",self.brand)
#         print("price is:",self.price)

# class Car(Vehicle):
#     def __init__(self, brand, price, model):
#         Vehicle.__init__(self,brand, price)
#         self.model = model
#     def show_car(self):
#         print("model is:", self.model)

# class Bike(Vehicle):
#     def __init__(self, brand, price,Bike_type):
#         Vehicle.__init__(self,brand, price)
#         self.Bike_type = Bike_type
#     def show_Bike(self):
#         print("bike type is:",self.Bike_type)

# class SportsVehicle(Car, Bike):
#     def __init__(self, brand, price, model, Bike_type, speed):
#         Car.__init__(self, brand, price, model)
#         self.Bike_type = Bike_type
#         self.speed = speed
#     def show_sports(self):
#         print("speed is:", self.speed)

# s = SportsVehicle("BMW", 4500000, "M4", "sports", 250)
# s.show_vehicle()
# s.show_car()
# s.show_Bike()
# s.show_sports()


 # Q8. Employee → Manager + Developer → TeamLead

# Create an Employee class with:# name # salary

# Create Manager and Developer classes that inherit from Employee.
# Create TeamLead that inherits from both Manager and Developer.

# Attributes:

# Employee → name, salary
# Manager → department
# Developer → programming_language
# TeamLead → team_size

# Methods:

# show_employee()
# show_manager()
# show_developer()
# show_teamlead()

# Take all values using input().


# class Employee:
#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary
#     def show_employee(self):
#         print("name :",self.name)
#         print("salary :",self.salary)

# class Manager(Employee):
#     def __init__(self, name, salary, department):
#         Employee.__init__(self, name, salary)
#         self.department = department
#     def show_manager(self):
#         print("department :", self.department)

# class Developer(Employee):
#     def __init__(self, name, salary, programming_language):
#         Employee.__init__(self, name, salary)
#         self.programming_language = programming_language
#     def show_developer(self):
#         print("programming_language :", self.programming_language)

# class TeamLead(Manager, Developer):
#     def __init__(self, name, salary, department, programming_language, team_size):
#         Manager.__init__(self,name, salary, department)
#         self.programming_language = programming_language
#         self.team_size = team_size
#     def show_teamlead(self):
#         print("team size:", self.team_size)

# t = TeamLead("jeni", 200000, "IT", "python", 5)
# t.show_employee()
# t.show_manager()
# t.show_developer()
# t.show_teamlead()
        
# Q9. Person → Student + Employee → WorkingStudent

# Create a Person class with: # name # age

# Create Student and Employee classes that inherit from Person.
# Create WorkingStudent that inherits from both Student and Employee.

# Attributes:

# Person → name, age
# Student → course
# Employee → salary
# WorkingStudent → working_hours

# Methods:

# show_person()
# show_student()
# show_employee()
# show_working_student()

# Use super() to initialize the parent attributes.

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def show_person(self):
#         print("Name:", self.name)
#         print("Age:", self.age)

# class Student(Person):
#     def __init__(self, name, age, course):
#         Person.__init__(self, name, age)
#         self.course = course
#     def show_student(self):
#         print("Course:", self.course)

# class Employee(Person):
#     def __init__(self, name, age, salary):
#         Person.__init__(self, name, age)
#         self.salary = salary
#     def show_employee(self):
#         print("Salary:", self.salary)

# class WorkingStudent(Student, Employee):
#     def __init__(self, name, age, course, salary, working_hours):
#         Student.__init__(self, name, age, course)
#         self.salary = salary
#         self.working_hours = working_hours
#     def show_working_student(self):
#         print("Salary:", self.salary)
#         print("Working Hours:", self.working_hours)

# w = WorkingStudent("Jeni", 20, "Python", 30000, 8)

# w.show_person()
# w.show_student()
# w.show_employee()
# w.show_working_student()

# Q10. Account → Saving + Current → PremiumAccount

# Create an Account class with:# account_holder # balance

# Create SavingAccount and CurrentAccount classes that inherit from Account.
# Create PremiumAccount that inherits from both SavingAccount and CurrentAccount.

# Attributes:

# Account → account_holder, balance
# SavingAccount → interest_rate
# CurrentAccount → overdraft_limit
# PremiumAccount → premium_benefit

# Methods:

# show_account()
# show_saving()
# show_current()
# show_premium()

# Take input from the user and display all details.

class Account:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance
    def show_account(self):
        print("Account Holder:", self.account_holder)
        print("Balance:", self.balance)

class SavingAccount(Account):
    def __init__(self, account_holder, balance, interest_rate):
        Account.__init__(self, account_holder, balance)
        self.interest_rate = interest_rate
    def show_saving(self):
        print("Interest Rate:", self.interest_rate)

class CurrentAccount(Account):
    def __init__(self, account_holder, balance, overdraft_limit):
        Account.__init__(self, account_holder, balance)
        self.overdraft_limit = overdraft_limit
    def show_current(self):
        print("Overdraft Limit:", self.overdraft_limit)

class PremiumAccount(SavingAccount, CurrentAccount):
    def __init__(self, account_holder, balance, interest_rate,
                 overdraft_limit, premium_benefit):
        SavingAccount.__init__(
            self, account_holder, balance, interest_rate
        )
        self.overdraft_limit = overdraft_limit
        self.premium_benefit = premium_benefit
    def show_premium(self):
        print("Overdraft Limit:", self.overdraft_limit)
        print("Premium Benefit:", self.premium_benefit)


p = PremiumAccount("Jeni", 100000, 7, 20000, "Airport Lounge")

p.show_account()
p.show_saving()
p.show_current()
p.show_premium()



