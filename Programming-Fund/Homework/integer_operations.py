import math
data = 0
for i in(0, 4):
    data = int(input())
    data += int(input())
    data /= int(input())
    data = math.floor(data)
    data *= int(input())
    print(data)
    break

