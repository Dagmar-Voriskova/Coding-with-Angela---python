print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? "))
tip = int(input("What percentage tip would you like to give? "))
people = int(input("How many people to split the bill? "))

count = (bill + (bill * tip / 100 )) / people
rounded = round(count, 2)

print(f"Each person should play ${rounded:.2f}")


