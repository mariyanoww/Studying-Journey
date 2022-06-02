chars = int(input())
sum = 0
for a in range(0, chars):
    char = str(input())
    sum += ord(char)
print(f'The sum equals: {sum}')

