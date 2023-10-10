cin = input()

smiley = False
frown = False 

for i in range(len(cin)-1):
    if cin[i] == ":" and cin[i+1] == "(":
        frown = True 
    if cin[i] == ":" and cin[i+1] == ")":
        smiley = True 

if frown and smiley:
    print("double agent")
elif frown:
    print("undead")
elif smiley:
    print("alive")
else:
    print("machine")