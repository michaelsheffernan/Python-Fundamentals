correct_number = 7
print("Welcome to the number guessing game!")
user_entry = int(input("Enter Guess: "))

while True:
    try:
        user_entry = int(input("Enter Guess: "))
    except:
        print("That's Not a Number!")
        continue

    if user_entry == correct_number:
        print("Congrats you win!")
        break
    elif user_entry > correct_number:
        print("Too High!")
    elif user_entry < correct_number:
        print("Too Low!")
