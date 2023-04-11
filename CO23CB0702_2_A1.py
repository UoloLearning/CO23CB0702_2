string = "apple pie"
found = False

for char in string:
    if char == 'a':
        found = True

if found:
    print("The letter 'a' was found in the string.")
else:
    print("The letter 'a' was not found in the string.")
