cin = list(map(int, input().split()))

fizz, buzz, l = cin[0], cin[1], cin[2]


for i in range(1, l+1):
    tmp= ""
    if i % fizz == 0:
        tmp += "Fizz"
    if i % buzz == 0:
        tmp+= "Buzz"
    if tmp == "":
        print(i)
    else:
        print(tmp)
