n = int(input())
rolls = []

for i in range(n):
    cin = input()
    rolls.append(cin)

bList = {}
for roll in rolls:
    for char in roll:
        if char in bList:
            for i in range(3):
                if roll[i] != char:
                    bList[char].add(roll[i])
        else:
            bList[char] = set()
            for i in range(3):
                if roll[i] != char:
                    bList[char].add(roll[i])


for c in bList:
    print(c, bList[c])