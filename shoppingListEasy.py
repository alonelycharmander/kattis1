
cin = input().split()

lists, length = int(cin[0]), int(cin[1])
ans = set(input().split())

for i in range(lists-1):
    tmpl = set(input().split())
    ans.intersection_update(tmpl)
ans = sorted(ans)
print(len(ans))
for item in ans:
    print(item)

