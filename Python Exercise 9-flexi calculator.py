def calculate(*numbers, **operations):
    total = sum(numbers)

    if operations.get("show_steps") == True:
        for value in numbers:
            print(f"Adding: {value}")

    if operations.get("round_result") == True:
        total = round(total, 2)

    return total


print(calculate(10.87, 45, 14.4628985, round_result=True, show_steps=True))
