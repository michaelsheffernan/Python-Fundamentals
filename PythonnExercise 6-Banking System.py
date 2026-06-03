import math

user_balance = 1000
pin_code = "1234"


def balance():
    print(f"Your Balnce is {user_balance}")
    return


def deposit_money(user_balance):
    deposit_amount = int(input("Please enter ammount for deposit: "))
    user_balance += deposit_amount
    print(f"Your balance is now {user_balance}")
    return user_balance


def withdraw_money(user_balance):

    withdraw_amount = int(input("Please enter ammount for withdrawl: "))
    if withdraw_amount > user_balance:
        print("You do not have enough funds to withdraw this ammount")
        withdraw_amount = int(input("Please enter ammount for withdrawl: "))
        user_balance -= withdraw_amount
        print(f"Your current balance is now {user_balance}")
    else:
        user_balance -= withdraw_amount
        print(f"Your current balance is now {user_balance}")
    return user_balance


print("Welcome to 365 Banking")
pin_entry = str(input("Please enter pin to continue: "))

if pin_entry == pin_code:
    print("Welcome")

    while pin_entry == pin_code:
        user_menu_selection = str(
            input("Which Service do you Require: Balance, Deposit or Withdraw: "))

        if user_menu_selection == "balance":
            balance()

        elif user_menu_selection == "deposit":
            user_balance = deposit_money(user_balance)

        elif user_menu_selection == "withdraw":
            user_balance = withdraw_money(user_balance)
        elif user_menu_selection == "quit":
            print("Thank you for using 365 Banking")
            break
else:
    print("Incorrect Pin")
