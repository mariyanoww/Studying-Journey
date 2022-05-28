coffee = 0
event = ""
while event.lower() != "end":
    event = input()
    if event.lower() == 'cat' or event.lower() == 'dog' or event.lower() == 'coding' or event.lower() == 'movie':
        if event.islower():
            coffee += 1
    if event.upper() == 'CAT' or event.upper() == 'DOG' or event.upper() == 'CODING' or event.upper() == 'MOVIE':
        if event.isupper():
            coffee += 2
if coffee > 5:
    print("You need extra sleep")
else:
    print(coffee)