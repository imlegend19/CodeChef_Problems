x, y = map(float, input().split())
c = y-x-0.5
if c >= 0 and x % 5 == 0:
    print(c)
else:
    print(y)

a = [float(x) for x in input().split()]
x = a[0]
y = a[1]
if x == y:
    print("%.2f" % y)
elif x < y and (x % 5 == 0):
    c = (y - x)-0.5
    print("%.2f" % c)
elif x < y and (x % 5 != 0):
    print("%.2f" % y)
elif x > y:
    print("%.2f" % y)
