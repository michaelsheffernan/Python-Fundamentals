import math

number = int(input("Please enter any number: "))

e_or_o_check = number % 2

if e_or_o_check == 0:
    print(f"{number} is even!")
else:
    print(f"{number} is odd!")
