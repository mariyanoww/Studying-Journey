txt = input()
numbers = txt.split(' ')
numbers = list(map(int, numbers))

evens = filter(lambda x: (x % 2 == 0), numbers)
evens = list(evens)
print(evens)
