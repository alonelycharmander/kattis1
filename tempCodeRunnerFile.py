import sys
mydt = {"2": "twenty", "3": "thirty", "4": "forty", "5": "fifty", 
          "6": "sixty", "7": "seventy", "8": "eighty", "9": "ninety"}
tens = {"10": "ten", "11": "eleven", "12": "twelve", "13": "thirteen", "14": "forteen",
        "15": "fifteen", "16": "sixteen", "17": "seventeen", "18": "eighteen", "19": "nineteen"}
ones = {"1": "one", "2": "two", "3": "three", "4": "four", "5": "five",
        "6": "six", "7": "seven", "8": "eight", "9": "nine", "0": "zero"}

def numToWord(word):
    if len(word) == 1:
        return ones.get(word)
    else:
        if int(word) < 20:
            return tens.get(word)
        else:
            tmp = ""
            tmp = mydt.get(word[0]) 
            if word[1] != "0":
                tmp = tmp + "-" + ones.get(word[1])
            return tmp

text = []
flag = False
for line in sys.stdin:
    tmp = line.split()
    for word in tmp:
        if word[0] in "0123456789":
            word = numToWord(word)
        if flag:
            tmpchar = word[0].upper() + word[1:]
            word = tmpchar
        print(word, end=" ")
        flag = False
    print()
    if word[-1] == ".":
        break
    flag = True
