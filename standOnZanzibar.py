tcase = int(input())

for i in range(tcase):
    cin = list(map(int, input().split()))
    nb = 0
    for i in range(len(cin)-1):
        if cin[i+1] == 0 or cin[i+1] == cin[i]:
            continue
        if cin[i+1] <= cin[i]*2:
            continue
        nb = nb + cin[i+1]-(cin[i]*2)

    print(nb)
