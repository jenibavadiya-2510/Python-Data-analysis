# Multiple example

# 20 Multiple Inheritance Practice Questions
# Basic Questions

# Q1. Create two classes Father and Mother. Create a Child class that inherits from both classes 
# and display methods from both parents.
# class Father:
#     def drive(self):
#         print("father can drive")
# class Mother:
#     def cook(self):
#         print("mother can cook")
# class Child(Father, Mother):
#     def play(self):
#         print("child can play")
# c = Child()
# c.drive()
# c.cook()
# c.play()

# Q2. Create classes Teacher and Student. Create a Person class that inherits from both and access
#  methods from both classes.Methods: teach(), study(), display()
# class Teacher:
#     def teach(self):
#         print("teacher can teach")
# class Student:
#     def study(self):
#         print("student can study")
# class Person(Teacher, Student):
#     def display(self):
#          print("diaplay person info")
# p = Person()
# p.teach()
# p.study()
# p.display()

# Q3. Create classes Animal and Bird. Create a FlyingAnimal class that inherits from both and
#  call methods from both parents.Methods: eat(), fly(), run().
# class Animal:
#     def eat(self):
#         print("Animal can eat")
# class Bird:
#     def fly(self):
#         print("Bird can fly")
# class FlyingAnimal(Animal, Bird):
#     def run(self):
#         print("Flying animal can run")
# f = FlyingAnimal()
# f.eat()
# f.fly()
# f.run()

# Q4. Create classes Father and Mother with different variables. Create Child and print all 
# variables.Methods: drive(), play_music(), display().
# class Car:
#     def drive(self):
#         print("Car can drive")
# class MusicSystem:
#     def play_music(self):
#         print("Music system can play music")
# class SmartCar(Car, MusicSystem):
#     def display(self):
#         print("Smart car has advanced features")
# s = SmartCar()
# s.drive()
# s.play_music()
# s.display()

#  Q5:
# class A:
#     def method_a(self):
#         print("A")
# class B:
#     def method_b(self):
#         print("B")
# class C(A, B):
#     def method_c(self):
#         print("C")
# obj = C()
# obj.method_a()
# obj.method_b()
# obj.method_c()

# Medium Questions

# Q6. Create School and Sports classes. Create Student that inherits from both and displays 
# academic and sports information.Methods: study(), play_sports(), display().
# class School:
#     def study(self):
#         print("study in school")
# class SportClasses:
#     def play_sports(self):
#         print("sport classes has play sports")
# class Display(School, SportClasses):
#     def display(self):
#         print("display information")
# d = Display()
# d.study()
# d.play_sports()
# d.display()

# Q7. Create Employee and Manager classes. Create TeamLeader that inherits from both and calls 
# methods from both classes.Methods: work(), show_department(), manage().
# class Employee:
#     def work(self):
#         print("Employee can work")
# class Department:
#     def show_department(self):
#         print("Employee belongs to IT department")
# class Manager(Employee, Department):
#     def manage(self):
#         print("Manager can manage the team")
# m = Manager()
# m.work()
# m.show_department()
# m.manage()

# Q8. Create Camera and Phone classes. Create SmartPhone class..Methods: take_photo(), call(), use_apps().
# class Camera:
#     def take_photo(self):
#         print("Camera can take photos")
# class Phone:
#     def call(self):
#         print("Phone can make calls")
# class SmartPhone(Camera, Phone):
#     def use_apps(self):
#         print("SmartPhone can use apps")
# s = SmartPhone()
# s.take_photo()
# s.call()
# s.use_apps()

# Q9. Create Teacher and Researcher classes. Create Professor that inherits from both and displays 
# teaching and research information.Methods: teach(), research(), display().
# class Teacher:
#     def teach(self):
#         print("Teacher can teach students")
# class Researcher:
#     def research(self):
#         print("Researcher can do research")
# class Professor(Teacher, Researcher):
#     def display(self):
#         print("Professor can teach and research")
# p = Professor()
# p.teach()
# p.research()
# p.display()

# Q10. Create BankAccount and Customer classes. Create AccountHolder that inherits from both and 
# displays account and customer details.Methods: deposit(), show_customer(), withdraw().
# class BankAccount:
#     def deposit(self):
#         print("deposit in bank account")
# class Customer:
#     def show_customer(self):
#         print("show customer details")
# class AccountHolder(BankAccount, Customer):
#     def withdraw(self):
#         print("account holder withdraw amount")
# a = AccountHolder()
# a.deposit()
# a.show_customer()
# a.withdraw()

# Medium → Advanced
# Q11. Create Academic and Sports classes. Create Student that inherits from both and 
# calculates/display student's academic and sports details.
# class Academic:
#     def study(self):
#         print("Student is good in studies")
# class Sports:
#     def play(self):
#         print("Student is good in sports")
# class Student(Academic, Sports):
#     def display(self):
#         print("Student has both academic and sports skills")
# s = Student()
# s.study()
# s.play()
# s.display()

# Q12. Create Father and Mother classes with __init__() methods. Create Child and properly 
# initialize attributes from both parent classes.
# class Father:
#     def __init__(self):
#         self.father_name = "Rajesh"

#     def show_father(self):
#         print("Father Name:", self.father_name)

# class Mother:
#     def __init__(self):
#         self.mother_name = "Priya"

#     def show_mother(self):
#         print("Mother Name:", self.mother_name)

# class Child(Father, Mother):
#     def __init__(self):
#         Father.__init__(self)
#         Mother.__init__(self)

#     def show_child(self):
#         print("Child is studying")
# c = Child()
# c.show_father()
# c.show_mother()
# c.show_child()

# Advanced Practice

# Q16. Create Employee and Department classes. Create Manager that inherits from both and displays
#  employee name, salary, and department.
# class Employee:
#     def name(self):
#         print("employee name: jeni")
# class Department:
#     def salary(self):
#         print("salary : 30000")
# class Manager(Employee, Department):
#     def department(self):
#         print("Department : it")
# m = Manager()
# m.name()
# m.salary()
# m.department()

# Q17. Create Login and Payment classes. Create OnlineUser that inherits from both and displays 
# login and payment information.Methods: login(), make_payment(), display()
# class Login:
#     def login(self):
#         print("User can login")
# class Payment:
#     def make_payment(self):
#         print("User can make payment")
# class OnlineUser(Login, Payment):
#     def display(self):
#         print("Online user can use login and payment")
# u = OnlineUser()
# u.login()
# u.make_payment()
# u.display()

# Q18. Create Product and Discount classes. Create FinalProduct that inherits from both and 
# calculates the final price after applying the discount.
# Methods: show_product(), calculate_discount(), final_price().
# class Product:
#     def show_product(self):
#         print("Product: Laptop")
# class Discount:
#     def calculate_discount(self):
#         print("Discount: 10%")
# class FinalProduct(Product, Discount):
#     def final_price(self):
#         print("Final Price: 45000")
# p = FinalProduct()
# p.show_product()
# p.calculate_discount()
# p.final_price()

# Q19. Create Student and Attendance classes. Create CollegeStudent that inherits from both and 
# displays student details and calculates attendance percentage.
# Methods: study(), calculate_attendance(), display().
# class Student:
#     def study(self):
#         print("Student can study")

# class Attendance:
#     def calculate_attendance(self):
#         total_days = 100
#         present_days = 85

#         percentage = (present_days / total_days) * 100
#         print("Attendance Percentage:", percentage, "%")

# class CollegeStudent(Student, Attendance):
#     def display(self):
#         print("College student is studying")
# s = CollegeStudent()
# s.study()
# s.calculate_attendance()
# s.display()

# Q20. Create Employee and Performance classes. Create SeniorEmployee that inherits from both 
# and calculates/display the employee's final performance score.
# Methods: work(), calculate_salary(), display_details().
# class Employee:
#     def work(self):
#         print("Employee is working")

# class Performance:
#     def calculate_performance(self):
#         score1 = 80
#         score2 = 90

#         final_score = (score1 + score2) / 2

#         print("Final Performance Score:", final_score)

# class SeniorEmployee(Employee, Performance):
#     def display_details(self):
#         print("Senior Employee")
# s = SeniorEmployee()
# s.work()
# s.calculate_performance()
# s.display_details()