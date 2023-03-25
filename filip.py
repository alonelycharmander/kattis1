cin = input()

num1, num2 = cin.split()

for i in range(2, -1, -1):
    if num1[i] > num2[i]:
        print(num1[::-1])
        break
    if num1[i] < num2[i]:
        print(num2[::-1])
        break