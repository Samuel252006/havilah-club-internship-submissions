# Day 11 — Introduction to Python
# Havilah Club Internship
# Student: Enyichukwu Samuel


# Exercise 1: Variables and Data Types

student_name = "Enyichukwu Samuel"
student_age = 20
student_height = 1.75
is_engineering_student = True

print("\n--- STUDENT PROFILE ---")
print("Student Name:", student_name)
print("Data Type:", type(student_name))

print("Student Age:", student_age)
print("Data Type:", type(student_age))

print("Student Height:", student_height, "metres")
print("Data Type:", type(student_height))

print("Engineering Student:", is_engineering_student)
print("Data Type:", type(is_engineering_student))


# Exercise 2: Arithmetic Calculator

print("\n--- ARITHMETIC CALCULATOR ---")

first_number = float(input("Enter the first number: "))
second_number = float(input("Enter the second number: "))

print("Sum:", first_number + second_number)
print("Difference:", first_number - second_number)
print("Product:", first_number * second_number)

if second_number != 0:
    print("Quotient:", first_number / second_number)
    print("Remainder:", first_number % second_number)
else:
    print("Quotient: Cannot divide by zero")
    print("Remainder: Cannot divide by zero")


# Exercise 3: Temperature Converter

print("\n--- TEMPERATURE CONVERTER ---")

celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = (celsius * 9 / 5) + 32

print("Temperature in Fahrenheit:", fahrenheit, "°F")

fahrenheit_input = float(input("Enter temperature in Fahrenheit: "))
kelvin = (fahrenheit_input - 32) * 5 / 9 + 273.15

print("Temperature in Kelvin:", kelvin, "K")


# Exercise 4: Robot Sensor Monitor

print("\n--- ROBOT SENSOR MONITOR ---")

robot_name = input("Enter Robot Name: ")
robot_id = input("Enter Robot ID: ")
sensor_name = input("Enter Sensor Name: ")

sensor_reading = float(input("Enter Sensor Reading: "))
operating_limit = float(input("Enter Operating Limit: "))

difference = operating_limit - sensor_reading

print("\n========== ROBOT SENSOR REPORT ==========")
print("Robot Name:", robot_name)
print("Robot ID:", robot_id)
print("Sensor Name:", sensor_name)
print("Sensor Reading:", sensor_reading)
print("Operating Limit:", operating_limit)
print("Difference from Limit:", difference)
print("========================================")
