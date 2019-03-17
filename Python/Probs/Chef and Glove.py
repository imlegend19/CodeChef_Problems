t = int(input())
ans = []
for _ in range(t):
    n = int(input())
    x = map(int,raw_input().split())
    y = map(int,raw_input().split())
    z = y[::-1]
    a = []
    b = []
    a[:]=[]
    b[:]=[]
    for i in range(len(x)):
        if (x[i]<=y[i]):
            a.append(1)
        else:
            a.append(0)
    for i in range(len(x)):
        if (x[i]<=z[i]):
            b.append(1)
        else:
            b.append(0)
    if (sum(a)==n==sum(b)):
        ans.append('both')
    elif (sum(a)==n):
        ans.append('front')
    elif (sum(b)==n):
        ans.append('back')
    else:
        ans.append('none')
for e in ans:
    print e