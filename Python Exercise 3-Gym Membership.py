age = int(input("Enter your age: "))
membership = input("Do you have a membership: ").lower().strip()

if age < 16:
    print("You are too young to enter the gym")
elif age >= 16 and membership == "yes":
    print("Access Granted, welcome to ANYTIME FITNESS")
elif age >= 16 and membership == "no":
    id = input("Do you have ID: ").lower().strip()
    if id == "yes":
        print("Temporary Access")
    else:
        print("No Access")
else:
    print("Access Denied")
