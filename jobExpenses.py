cin = int(input())

expen = list(map(int, input().split()))
ans = 0 

for charge in expen:
    if charge < 0:
        ans = ans + (-1*charge)
print(ans)