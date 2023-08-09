r, c, zr, zc = list(map(int, input().split()))


moja = []

for i in range(r):
    row = input()
    moja.append(row)

res = []

for row in moja:
    i = 0 
    while i < zr:
        for j in range(c):
            k = 0 
            while k < zc:
                print(row[j], end="")
                k += 1
        print()
        i += 1 
