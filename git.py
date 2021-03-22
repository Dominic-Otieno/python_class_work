#BEFORE
for number in range(1,55):
...    if number %9==0 or number %8==0:
...       print("Thats Graet Buddy!")
...    if number %8==0:
...       print("Good Trial AsuP!")
...    if number %9==0:
...       print("Cool Man!")
...    else:
...       print([number])
#AFTER
for number in range(1,55):
...    print(f"Test code, number = {number}")
...    if number %8==0 and number %9==0:#Changed or to and since all conditions are needed
...       print("Who are you?")
...    elif number %8==0:#changed if to elif so doesn't along with line above.
...       print("You Can't see me")
...    elif number %9==0:# change if to elif so doesn't execute with original statement.
...       print("You are all Caught UP!")
...    else:#when none of the conditions are met it executes.
...       print(number)# removed [] which were displaying numbers as list.
