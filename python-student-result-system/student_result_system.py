# Student Result Management System

print("STUDENT RESULT MANAGEMENT SYSTEM")

name = input("Enter Student Name: ")
roll_no = input("Enter Roll Number: ")

m1 = int(input("Enter Mark 1: "))
m2 = int(input("Enter Mark 2: "))
m3 = int(input("Enter Mark 3: "))

total = m1 + m2 + m3
average = total / 3

if average >= 75:
    grade = "A"
elif average >= 60:
    grade = "B"
elif average >= 40:
    grade = "C"
else:
    grade = "Fail"
print("\nResult:")
print("Name:", name)
print("Roll No:", roll_no)
print("Total:", total)
print("Average:", average)
print("Grade:", grade)