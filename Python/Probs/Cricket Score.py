from copy import deepcopy
n = int(input())
runs = []
wickets = []

for _ in range(n):
    x, y = map(int, input().split())
    runs.append(x)
    wickets.append(y)

flag = 0
x1 = deepcopy(runs)
x1.sort()
if runs == x1:
    flag = 1
else:
    print("NO")

y1 = deepcopy(wickets)
y1.sort()
if flag == 1:
    if wickets == y1 and max(wickets) <= 10 and wickets.count(10) < 2:
        print("YES")
    else:
        print("NO")

# print(runs, wickets)