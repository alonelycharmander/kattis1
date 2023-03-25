p1 = input()
p2 = input()

dif = 0

for i in range(len(p1)):
    if p1[i] != p2[i]:
        dif += 1
print(2**dif)
