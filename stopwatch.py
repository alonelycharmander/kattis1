taps = int(input())
res = 0
start = True 
for i in range(taps):
    tmp = int(input())
    if start:
        st = tmp
    if not start:
        res = res + (tmp - st)
    start = not start

if start: 
    print(res)
else:
    print("still running")
