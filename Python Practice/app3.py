game_active = True
while game_active:
    txtbox = input('> ')
    if txtbox.upper() == 'HELP':
        print("""
        start - to start the car
        stop - to stop the car
        help - to get the list of commands
        quit - to exit the program""")
    elif txtbox.upper() == 'START':
        print('Car started... Ready to go!')
    elif txtbox.upper() == 'STOP':
        print('Car stopped.')
    elif txtbox.upper() == 'QUIT':
        break
    else:
        print('Error... Does not compute!')
else:
    print("Your car crashed. You've been terminated.")


secret_number = 9
guess_times = 0
guess_limit = 3
while guess_times < guess_limit:
    guess = int(input("Guess: : "))
    guess_times += 1
    if guess == secret_number:
        print("You win!")
        break
else:
    print("Sorry, you ran out of tries.")
