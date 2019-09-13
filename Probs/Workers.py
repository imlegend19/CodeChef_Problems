n = int(input())      # c = [1,3,4,6,8]          type = [1,2,1,2,3]
c = [int(x) for x in input().split()]
type = [int(x) for x in input().split()]
ans = []
c1 = []
c2 = []
c3 = []
for i in range(len(type)):
    if type[i] == 1:
        c1.append(c[i])
    elif type[i] == 2:
        c2.append(c[i])
    elif type[i] == 3:
        c3.append(c[i])
if len(c1) == 0 or len(c2) == 0 or (len(c1) == 0 and len(c2) == 0):
    ans.append(min(c3))
else:
    w1 = min(c1) + min(c2)
    if len(c3) != 0:
        w2 = min(c3)
        ans.append(min(w1, w2))
    else:
        ans.append(w1)
for e in ans:
    print(e)