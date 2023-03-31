import sys
def daylight(riseh, risem, seth, setm):
    min_rise = (int(riseh)*60) + int(risem)
    min_set = (int(seth)*60) + int(setm)
    mindif = min_set-min_rise
    hours = mindif // 60
    min = (mindif-(hours*60))
    #print(min_rise, min_set, mindif, hours, min)
    print(hours, "hours", min, "minutes")

cin = input()
tmp = cin.split()
for line in sys.stdin:
    if len(tmp[3]) < 5:
        hrise = tmp[3][0]
        mrise = tmp[3][2:]

    else:
        hrise = tmp[3][0:2]
        mrise = tmp[3][3:]
    hset = tmp[4][0:2]
    mset = tmp[4][3:]
    print(tmp[0], tmp[1], tmp[2], end=" ")
    daylight(hrise, mrise, hset, mset)
    cin = input()
    tmp = cin.split()