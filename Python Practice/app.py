course = "this is a test sentence."
import math
y = -2.9
print(math.ceil(y))
print(math.floor(y))
print(abs(y))
print(round(y))

ishot = True
iscold = True

if ishot and iscold:
    print("It can't be both, you liar! Reality does not permit paradoxes!")
elif iscold:
    print("It's a cold day indeed.")
    print("Wear warm clothes or you'll become a snowman and freeze to death before you know it.")
elif ishot:
    print("It is indeed hot!")
    print("Make sure to stay hydrated, hydro homie!")
else:
    print("It's a lovely day.")

print("this is just a test")
print()
print()
house_price = 1000000
good_credit = False

if good_credit:
    downpay = house_price * 0.10
    excess_message = "Congratulations, you have good credit."
    onlyword = " only"
else:
    downpay = house_price * 0.20
    excess_message = "We're sorry to inform you that you don't have good credit."
    onlyword = ""

input("Press Enter to continue...")
print(excess_message)
print(f"You need to make a down payment of{onlyword} ${int(downpay)}.")
print()
print("Just a test " + str(downpay))

















