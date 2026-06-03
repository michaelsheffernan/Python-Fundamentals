password = "Admin123"
user_entry = str(input("Enter Password: "))
attempt_count = 0


while True and attempt_count < 3:
    if user_entry == "Admin123":
        print("Welcome Admin")

        break
    else:
        print("Incorrect Password")
        attempt_count += 1
        user_entry = str(input("Enter Password: "))
