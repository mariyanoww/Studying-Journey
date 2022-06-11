offers = str(input())
beggars = int(input())
offer = offers.split(', ')
offer = [int(i) for i in offer]
final = []
index = 0
while index < beggars:
    current = 0
    for i in range(index, len(offer), beggars):
        current += offer[i]
    index += 1
    final.append(current)
    continue
print(final)