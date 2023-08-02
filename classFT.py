s1 = list(input())
s2 = list(input())

ans = ""

while s1 or s2:
    if s1:
        if len(s2) == 0 or s1[0] <= s2[0]:
            ans += s1.pop(0)
    if s2:
        if len(s1) == 0 or s2[0] < s1[0]:
            ans += s2.pop(0)
print(ans)