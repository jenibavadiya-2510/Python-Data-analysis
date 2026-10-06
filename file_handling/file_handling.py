

# file = open("demo.txt", "r")
# data = file.readlines()
# print(data)
# file.close()

# file = open("demo.txt", "a")
# file.write("\n hello jeni")
# file.close()

# with open("student.txt", "a") as file:
#     file.write("Jeni\n")
#     file.write("Python\n")
#     file.write("sql\n")
#     file.write("Data Analyst")

# Basic
# Create a file named data.txt and write "Hello Python" into it.
# file = open("data1.txt", "w")
# file.write("hello python")
# file.close()

# Read and display the complete contents of a file.
# file = open("data1.txt", "r")
# data = file.readlines()
# print(data)
# file.close()

# file = open("data1.txt", "a")
# file.write("\nhello java")
# file.close()

# Read a file line by line using readline().
# file = open("data1.txt", "r")
# data = file.readline()
# print(data)
# file.close()

# Read all lines of a file using readlines().
# file = open("data1.txt", "r")
# data = file.readlines()
# print(data)
# file.close()

# Append "Welcome to Python" to an existing file.
# file = open("data1.txt", "a")
# file.write("\n Welcome to python")
# file.close()

# Medium
# Write 5 student names into a file and then read them.
# file = open("stu.txt", "w")
# file.write("Amit\n")
# file.write("Raj\n")
# file.write("Ankit\n")
# file.write("John\n")
# file.write("Jeni\n")
# file.close()

# Count the number of lines in a text file.
# file = open("stu.txt", "r")
# count = 0
# for line in file:
#     count += 1
# print("total lines:", count)
# file.close()

# Count the number of words in a text file.
# file = open("stu.txt", "r")
# count = 0
# for line in file:
#     words = line.split()
#     count += len(words)

# print("total words:", count)
# file.close()

# # Program 1: File બનાવો અને તેમાં લખો (w mode)
# file = open("emp.txt", "w")
# file.write("jeni")
# file.close
# print("data saved")

# # # Program 2: File માંથી વાંચો (r mode)
# file = open("emp.txt", "r")
# file.read()
# file.close()
# print("data saved")

# Program 3: નવો Data ઉમેરો (a mode)
# file = open("emp.txt", "a")
# file.write("\n jensi")
# file.close()

# Program 4: Line by Line વાંચો
# file = open("emp.txt", "r")
# for line in file:
#     print(line)
# file.close()

# Program 5: readlines()
# file = open("emp.txt", "r")
# data = file.readlines()
# print(data)
# file.close()

# Program 6: strip() નો ઉપયોગ
# file = open("emp.txt","r")
# for line in file:
#     print(line.strip())
# file.close()

# task
# name = input("enter name :")
# file = open("emp.txt","a")
# file.write(name + "\n")
# file.close()
# print("data saved")

# # 1. File બનાવો
# file = open("stu1.txt","w")

# file.write("jeni")

# file.close()
# print("data add")

# # 2. File વાંચો
# file = open("stu1.txt","r")
# data = file.read()
# print(data)
# file.close()
# print("file read")

# # 3. File માં Data ઉમેરો
# name = input("enter name :")
# file = open("stu1.txt","a")
# file.write(name + "\n")
# file.close()
# print("name add")

# # 4. ત્રણ નામ Save કરો
# file = open("stu1.txt","a")

# for name in range(3):
#     name = input("enter name :")
#     file.write(name + "\n")

# file.close()

# # 5. બધી Lines Print કરો
# file = open("stu1.txt","r")

# data = file.readlines()
# print(data)
# file.close()

# # 6. કુલ કેટલા Names છે?
# file = open("stu1.txt","r")
# count = 0

# for line in file:
#      line.count(name)
#      count += 1
# print("total names :",count)

# file.close()

# # 7. Search Name

# file = open("stu1.txt","r")
# name = input("enter name :")
# data = file.read()
# if name.lower() in data:
#      print("found")
# else:
#      print("not found")
# file.close()

# # 8. Delete Name
# file = open("stu1.txt","r")

# name = input("enter name :")

# data = file.readlines()
# file.close()

# file = open("stu.txt","w")

# found = False

# for line in data:
#       if line.strip().lower() != name.lower():
#         file.write(line)
#       else:
#         found = True

# file.close()

# if found:
#     print("Name Deleted Successfully")
# else:
#     print("Name Not Found")

# # 9. Update Name
# file = open("stu1.txt","r")

# old_name = input("enter old name :")
# new_name = input("enter new name :")

# data = file.readlines()
# file.close()

# file = open("stu1.txt","w")

# for line in data:
#     if line.strip() == old_name:
#         file.write(new_name + "\n")
#     else:
#         file.write(line)

# file.close()
# print("Name Updated Successfully")