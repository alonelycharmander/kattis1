points = list(map(int, input().split()))

x, y = points[0], points[1]
x1, y1 = points[2], points[3]
x2, y2 = points[4], points[5]


if(abs(x1 -x) < abs(x2 - x)):
    px = x1
else:
    px = x2

if (abs(y1 - y) < abs(y2 -y)):
    py = y1
else:
    py = y2

