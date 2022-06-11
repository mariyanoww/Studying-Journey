a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
card = str(input())
card_1 = card.split(' ')
for asd in card_1:
    card_2 = asd.split('-')
    team = card_2[0]
    number = card_2[1]
    if team == 'A' and a.count(int(number)):
        a.remove(int(number))
    if team == 'B' and b.count(int(number)):
        b.remove(int(number))
    if len(a) < 7 or len(b) < 7:
        break
print(f'Team A - {len(a)}; Team B - {len(b)}')
if len(a) < 7 or len(b) < 7:
    print('Game was terminated')
