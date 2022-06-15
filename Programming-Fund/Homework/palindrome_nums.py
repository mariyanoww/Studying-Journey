txt = input()
numbers = txt.split(', ')

for x in numbers:
    current_num = list(x)
    current_num = list(map(int, current_num))
    reversed_current_num = list(reversed(current_num))
    if current_num == reversed_current_num:
        print('True')
    else:
        print('False')
