n = int(input())
for n in range(0, n):
    data = input()
    if "_" in data or "," in data or "." in data:
        print(f'{data} is not pure!')
    else:
        print(f'{data} is pure.')