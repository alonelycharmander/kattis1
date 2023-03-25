
def list_maker(list: nums):

    flag = True 
for i in range(len(nums)-1):
    if nums[i]+1 != nums[i+1]:
        if not flag:
            err = err + "-" + str(nums[i]) + ","
        else:
            err = err + " " + str(nums[i]) + ","
        flag = True 
    else:
        if flag:
            err = err + " " + str(nums[i]) 
            flag = False
    if(curr[-1] == ","):
        curr = curr[0: len(curr)-1]


cin = input()
n, errors = cin.split()
ans = list(map(int, input().split()))

errors = int(errors)
err = "Errors: "
curr = "Correct: "

dp = []
index = 0
flag = True 
for i in range(1, int(n)+1):
    if i not in ans:
        dp.append(i)
    if index == len(ans):
        break
ans.append(-1)
dp.append(-1)



for i in range(len(dp)-1):
    if dp[i]+1 != dp[i+1]:
        if not flag:
            curr = curr + "-" + str(dp[i]) + ","
        else:
            curr = curr + " " + str(dp[i]) + ","
        flag = True 
    else:
        if flag:
            curr = curr + " " + str(dp[i]) 
            flag = False

if(curr[-1] == ","):
    curr = curr[0: len(curr)-1]
if(err[-1] == ","):
    err = err[0: len(err)-1]
index_curr = curr.count(" ")
index_err = err.count(" ")

tmp = err.split()
tmp[-2] = tmp[-2][0:-1]
tmp.insert(-1, "and")
err2 = " ".join(tmp)


tmp2 = curr.split()
tmp2[-2] = tmp2[-2][0:-1]
tmp2.insert(-1, "and")
curr2 = " ".join(tmp2)
print(err2)
print(curr2)