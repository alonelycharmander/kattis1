import sys
guess = 500
print(guess)
for ans in sys.stdin:
    if ans == "correct":
        break
    if ans == "lower":
        guess = guess//2
    else:
        guess = (guess-100)