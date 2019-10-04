# The following block of code is a For Loops Range function testing
for number in range(1, 10):
  print("Attempting", str(number) + (number * "."))
print()
numeroo = 2
for numero in range(200):
  print("Attempting", numero + 1, (numeroo) * '.')
  numeroo += 1

# -------------------------------------------------------------------
  

# The following block of code makes large letters L or F show up on screen, built of 'x's.
print()

pressed = input('Type L or F to show it on the screen! ').lower()

if pressed == "f":
  numbers = [5, 2, 5, 2, 2]
  for x in numbers:
    output = ''
    for y in range(x):
      output += 'x'
    print(output)
elif pressed == "l":
  numbers = [2, 2, 2, 2, 5]
  for i in numbers:
    output = ''
    for ii in range(i):
      output += 'x'
    print()
else:
  print('Error... does not compute!')
  
# ----------------------------------------------------------------------------------------
