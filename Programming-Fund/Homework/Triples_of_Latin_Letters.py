num = int(input())
list4e = []
for i in range(0, num):
    for k in range(0, num):
        for j in range(0, num):
            list4e.append(chr(97 + i) + chr(97 + j) + chr(97 + k))
list4e.sort()
print('\n'.join(map(str, list4e)))