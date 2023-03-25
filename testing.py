cin = int(input())
flag = True 

while flag:
    hours = 0
    speedl = 0
    for i in range(cin):
        uin = list(map(int, input().split()))
        speedl = speedl + uin[0]*(uin[1]-hours)
        
        hours = uin[1]
    print(speedl, "miles")
    cin = int(input())
    if cin == -1:
        flag = False