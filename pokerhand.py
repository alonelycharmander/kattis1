cin = input()

hand = cin
hand = hand.split()

nhand = []

for card in hand: 
    nhand.append(card[0])

ans = 1
tmp = set(nhand)

for card in tmp:
    ans = max(ans, nhand.count(card))
print(ans)