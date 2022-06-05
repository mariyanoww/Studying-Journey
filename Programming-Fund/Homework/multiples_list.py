factor = int(input())
count = int(input())
cosmos = 0
cosmos2 = []
for a in range(0, count):
    cosmos += factor
    cosmos2.append(cosmos)
print(cosmos2)