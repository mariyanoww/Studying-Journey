while True:
    word = str(input())
    if word == "SoftUni":
        continue
    if word == "End":
        break
    for i in word:
        print(i+i, end='')
    print()