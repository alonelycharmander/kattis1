s = input()

code = input()
ans = ''

for i in range(len(code)+1):
    
    if i % 3 == 0 and i != 0:
        index = int(code[i-3:i])
        print(s[index-1], end="")