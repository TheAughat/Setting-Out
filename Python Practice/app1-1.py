# The following block of code is a command line function app that takes in four commands, start, stpo, help, and quit
# and prints responses on the terminal
command = ""
running = False

while True:
  command = input('> ').lower()
  if command == 'start':
    if running:
      print('The car has already been started.')
    else:
      print('The car has started!')
      running = True
  elif command == 'stop':
    if not running:
      print('The car has not been started in the first place.')
    else:
      print('The car has stopped.')
      running = False
  elif command == 'help':
    print('''
start - to start the car
stop - to stop the car
help - to check the list of commands
quit - to exit the program
    ''')
  elif command == 'quit':
    break
  else:
    print('Error... does not compute.')
    
# --------------------------------------------------------------------------------------------------------------
