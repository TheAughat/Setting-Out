# The following block of code is a While loop that allows the user to guess a number. The loop terminates if they get it right.
# If they don't get it right, they're allowed three tries before the loop automatically terminates with a message

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
