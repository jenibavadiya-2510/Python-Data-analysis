# example
# class Dog:
#     def sound(self):
#         print("Dog says: Woof Woof")
# class Cat:
#     def sound(self):
#         print("Cat says: Meow Meow")
# d = Dog()
# c = Cat()

# d.sound()
# c.sound()

# Basic Questions
# Create a Person class with name and age using __init__(). Create an object and display 
# both details.

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def show(self):
#         print("name :", self.name)
#         print("age :", self.age)

# p = Person("jeni", 21)
# p.show()

# Create a Student class with name, roll_no, and marks using __init__(). Create two
# objects and display their details.

# class Student:
#     def __init__(self,name,roll_no):
#          self.name = name
#          self.roll_no = roll_no
#     def show_student(self):
#         print("name :",self.name)
#         print("roll no :",self.roll_no)

# s = Student("jeni", 7)
# s.show_student()
         
# Create an Employee class with name, salary, and department using __init__(). Add a show()
#  method to display all details.

# class Employee:
#     def __init__(self, name, salary, department):
#         self.name = name
#         self.salary = salary
#         self.department = department
#     def show(self):
#         print("name :",self.name)
#         print("salary :",self.salary)
#         print("department :",self.department)
# e = Employee("priya", 25000, "IT")
# e.show()

# Create a Product class with name, price, and quantity using __init__(). Add a method to
#  calculate and display the total price.

# class Product:
#     def __init__(self, name, price, quantity):
#         self.name = name
#         self.price = price
#         self.quantity = quantity
#     def total_price(self):
#         total = self.price * self.quantity
#         print("Product :", self.name)
#         print("Total Price :", total)
# p = Product("laptop", 50000, 2)
# p.total_price()

# Create a BankAccount class with account_no, name, and balance using __init__(). 
# Add a show() method to display account details.

# class BankAccount:
#     def __init__(self, account_no, name, balance):
#         self.account_no = account_no
#         self.name = name
#         self.balance = balance
#     def show(self):
#         print("Account No :", self.account_no)
#         print("Name :", self.name)
#         print("Balance :", self.balance)

# a = BankAccount(101, "Jeni", 50000)
# a.show()

# Create a Hospital Management System:
# class Person:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
       
#     def show(self):
#         print("name is :",self.name)
#         print("age is :",self.age)

# class Doctor(Person):
#     def __init__(self,name,age,specialization,experience):
#         super().__init__(name,age)
#         self.specialization = specialization
#         self.experience = experience

#     def show_method(self):
#         print("specialization :",self.specialization)
#         print("experience :",self.experience)

# class Patient(Person):
#     def __init__(self,name,age,disease,room_number):
#         super().__init__(name,age)
#         self.disease = disease
#         self.room_number = room_number

#     def display(self):
#         print("disease :",self.disease)
#         print("room_number :",self.room_number)

# class Surgeon(Doctor):
#     def __init__(self,name,age,specialization,experience,operation_type):
#         super().__init__(name,age,specialization,experience)
#         self.operation_type = operation_type

#     def show_surgeon(self):
#         print("operation type :",self.operation_type)

# a = Doctor("jevan",45,"ortologist",3)
# a.show()
# a.show_method()

# b = Patient("suvi",40,"fever",678)
# b.show()
# b.display()

# c = Surgeon("jensi",50,"eye_surgeon",12,"eye")
# c.show()
# c.show_method()
# c.show_surgeon()


# smart home system

# class Device:
#     def __init__(self,device_name,status):
#         self.device_name = device_name
#         self.status = status

#     def show_device(self):
#         print("device name :",self.device_name)
#         print("status :",self.status)

# class Light(Device):
#     def __init__(self,device_name,status,brightness):
#         super().__init__(device_name,status)
#         self.brightness = brightness
    
#     def turn_on(self):
#         print("brightness :",self.brightness)

# class Fan(Device):
#     def __init__(self,device_name,status,speed):
#         super().__init__(device_name,status)
#         self.speed = speed

#     def Fan_on(self):
#         print("speed :",self.speed)

# class SmartFan(Fan):
#     def __init__(self,device_name,status,speed,voice_control):
#         super().__init__(device_name,status,speed)
#         self.voice_control = voice_control

#     def Smartfan_off(self):
#         print("voice control :",self.voice_control)

# p = Light("TV","off","Light")
# p.show_device()
# p.turn_on()

# q = Fan("AC","on","Full")
# q.show_device()
# q.Fan_on()

# r = SmartFan("fan","on","medium","no")
# r.show_device()
# r.Fan_on()
# r.Smartfan_off()

# food ordering system
# class Food:
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price
#     def order(self):
#         print("Food ordered")

# class Pizza(Food):
#     def __init__(self, name, price, size):
#         super().__init__(name, price)
#         self.size = size
#     def order(self):
#         print("pizza ordered")
#         print("name :", self.name)
#         print("price :", self.price)
#         print("size :",self.size)

# class Burger(Food):
#     def __init__(self, name, price, type):
#         super().__init__(name, price)
#         self.type = type
#     def order(self):
#         print("Burger ordered")
#         print("name :", self.name)
#         print("price :", self.price)
#         print("type :",self.type)

# class Dessert(Food):
#     def __init__(self, name, price, type, quantity):
#         super().__init__(name, price)
#         self.type = type
#         self.quantity = quantity
#     def order(self):
#         print("Dessert ordered")
#         print("name :", self.name)
#         print("price :", self.price)
#         print("type :",self.type)
#         print("quantity :", self.quantity)

# p = Pizza ("Margherita", 250, "Medium")
# b = Burger("Chesse burger", 180, "veg")
# d = Dessert("chocolava cake", 150, "cake", 2)

# p.order()
# print()
# b.order()
# d.order()

# payment method system

# class Payment:
#     def __init__(self, amount):
#         self.amount = amount
#     def pay(self):
#         print("payment method:")

# class CreditCard(Payment):
#     def __init__(self, amount, card_number):
#         super().__init__(amount)
#         self.card_number = card_number
#     def pay(self):
#         print("Use credit card")
#         print("amount :", self.amount)
#         print("card number :", self.card_number)

# class UPI(Payment):
#     def __init__(self, amount, upi_id):
#         super().__init__(amount)
#         self.upi_id = upi_id
#     def pay(self):
#         print("Use UPI :")
#         print("amount :", self.amount)
#         print("upi id :", self.upi_id)

# class Cash(Payment):
#     def __init__(self, amount, cash_received):
#         super().__init__(amount)
#         self.cash_received = cash_received
#     def pay(self):
#         print("Use cash:")
#         print("amount :", self.amount)
#         print("cash_received", self.cash_received)

# c = CreditCard(5000, "1234-5678-9012")
# u = UPI(2500, "jeni@upi")
# C = Cash(1000, 1500)

# c.pay()
# print()
# u.pay()
# C.pay()

# Notification System
# class Notification:
#     def __init__(self, message):
#         self.message = message
#     def send(self):
#         print("Notification system")

# class EmailNotification(Notification):
#     def __init__(self, message, email):
#         super().__init__(message)
#         self.email = email
#     def send(self):
#         print("Email notification :")
#         print("message :", self.message)
#         print("email :", self.email)

# class SMSNotification(Notification):
#     def __init__(self, message, phone_number):
#         super().__init__(message)
#         self.phone_number = phone_number
#     def send(self):
#         print("sms notification")
#         print("message :", self.message)
#         print("phone number:", self.phone_number)

# class PushNotification(Notification):
#     def __init__(self, message, device_name):
#         super().__init__(message)
#         self.device_name = device_name
#     def send(self):
#         print("push notification")
#         print("message :", self.message)
#         print("device name :", self.device_name)

# e = EmailNotification("Your order has been confirmed", "jeni@gmail.com")
# s = SMSNotification("Your OTP is 1234", 9876543210)
# p = PushNotification("You have a new notification", "Samsung Galaxy")

# e.send()
# s.send()
# p.send()