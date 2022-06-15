password = input()
numbers = list(password)
valid = False
digits = 0
length = True
dig_and_letters = True
digits_two = False
gth = len(numbers)
for i in numbers:
    if 6 > gth or gth > 10:
        length = False

    if not i.isalnum():
        dig_and_letters = False

    if i.isnumeric():
        digits += 1

    if digits >= 2:
        digits_two = True

    if length and digits_two and dig_and_letters:
        valid = True
if not length:
    print("Password must be between 6 and 10 characters")
if not dig_and_letters:
    print("Password must consist only of letters and digits")
if not digits_two:
    print("Password must have at least 2 digits")
if valid:
    print("Password is valid")
