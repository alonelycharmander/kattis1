at_bat = input()

bats = list(map(int, input().split()))
bat_total = 0
non_walks = 0
for bat in bats:
    if bat != -1:
        bat_total += bat
        non_walks += 1 
print(bat_total/non_walks)