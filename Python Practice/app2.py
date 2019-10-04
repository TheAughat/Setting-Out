unit = input("Which unit of measurement do you want to use? (lbs or kg): ")
if unit == "kg" or unit == "KG" or unit == "Kg":
    unit = "kg"
elif unit.lower() == "lbs":
    unit = "lbs"
else:
    print("Please enter a proper value (kg or lbs).")

if unit == "kg" or unit == "lbs":
    weight = int(input(f"Now please enter your weight: (in {unit}): "))
    if unit == "kg":
        weight = round(weight * 2.205)
        unit = "lbs"
    elif unit == "lbs":
        weight = round(weight / 2.205)
        unit = "kg"
    print(f"Your weight is {weight}{unit}.")
else:
    print("Next time please pay better attention to the rules.")

print()

print()

print()


high_income = False
good_credit = True

if good_credit and high_income:
    print("Eligible for major loan.")
elif good_credit and not high_income:
    print("Eligible for minor loan.")
elif good_credit or high_income:
    print("Eligible for micro loan.")
else:
    print("You're not even eligible for a fucking loan.")


print()


name = input("Enter your name: ")

if len(name) < 3:
    print("Sorry, the username must be over three characters long.")
elif len(name) > 12:
    print("Sorry, the character limit for your username is 12 characters.")
else:
    print(f"Thank you, {name.title()}. You will be redirected shortly...")
print()
print()
