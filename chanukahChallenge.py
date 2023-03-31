n = int(input())

for i in range(n):
    cin = list(map(int, input().split()))
    start, end = cin[0], cin[1]
    candles = 0
    for j in range(1, end+1):
        candles = candles + j
        if j == end:
            candles += j
    
    print(start, candles)
