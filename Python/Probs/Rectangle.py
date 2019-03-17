t = int(input())
list = list()
for i in range(t):
    a = [map(int,input().split())]
    if (a[0] == 0 and a[2] == 0 and a[3] == 0 and a[1] == 0):
        y = "NO"
    elif (a[0]==a[1] and a[2]==a[3]) or (a[0]==a[2] and a[1]==a[3]) or (a[0]==a[3] and a[1]==a[2]):
        y = "YES"
    else:
        y = "NO"
    list.append(y)
for j in list:
    print(j)

