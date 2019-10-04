numbers = [5, 2, 5, 2, 2]

for x_count in numbers:
    output = ""
    for count in range(x_count):
        output += "x"
    print(output)

print()

print('Writes the times table for anything till times 10. Enter "please stop" to quit.')
while True:
    print()
    tables = input("Which number do you want to see the tables of? ")
    number = 0
    if tables.lower() == "please stop":
        print()
        print("Alright, kiddo. Enough math for now.")
        print()
        break
    else:
        for times10 in range(int(tables), int(tables) * 11, int(tables)):
            number += 1
            print(f'{int(tables)} x {number} = {times10}')
