t = int(input())
ans = []
a = []   # a = [[100,5,10],[100,1,50]]
for _ in range(t):
    a[:] = []
    n = int(input())
    for _ in range(n):
        x = map(int, input().split())
        a.append(x)
    loss_count = 0
    for i in range(len(a)):
        y = float(a[i][0]*a[i][2])/100
        p_new = a[i][0] + float(y)
        p_new_disc =(p_new*a[i][2])/100
        loss = (p_new_disc - y)*a[i][1]
        loss_count += loss
    ans.append(loss_count)
for e in ans:
    print(e)
