deck = list(map(str, input().split(' ')))
final_deck = []
shuffles = int(input())
pre_final_deck = deck
for if4o in range(0, shuffles):
    deck1 = pre_final_deck[0:int(len(deck) / 2)]
    deck2 = pre_final_deck[int(len(deck) / 2):]
    pre_final_deck = []
    for ilian in range(0, len(deck1)):
        pre_final_deck.append(deck1[ilian])
        pre_final_deck.append(deck2[ilian])
final_deck = pre_final_deck
print(final_deck)
