cin = input()

judges, scores = cin.split()


arr = []
for i in range(int(scores)):
    score = int(input())
    arr.append(score)


min_score = (sum(arr) + (int(judges) - int(scores)) * -3)/int(judges)
max_score = (sum(arr) + (int(judges) - int(scores)) * 3)/int(judges)
print(min_score, max_score)