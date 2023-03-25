cin = input()

cin = cin.split()

if (cin[0] == "OCT" and cin[1] == "31") or (cin[0] == "DEC" and cin[1] == "25"):
    print("yup")
else:
    print("nope")