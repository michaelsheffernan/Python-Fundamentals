import math

print("Welcome to the Super Calc!")

first_number = int(input("Enter first number: "))
second_number = int(input("Enter second number: "))
operation = input("Chose your operation; + , - , * , / : ")

if operation == "+":
    result_1 = first_number + second_number
elif operation == "-":
    result_1 = first_number - second_number
elif operation == "*":
    result_1 = first_number * second_number
elif operation == "/":
    if second_number == 0:
        print("Math Error")
    else:
        result_1 = first_number / second_number


print(f"Result: {result_1}")
