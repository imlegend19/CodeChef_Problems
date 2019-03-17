import math
t = int(input())
ans = []
for i in range(t):
    x = [int(x) for x in input().split()]
    y = x[0] + x[1]
    c = math.floor(y/x[2])
    if c % 2 == 0:
        ans.append('CHEF')
    else:
        ans.append('COOK')

for e in ans:
    print(e)
