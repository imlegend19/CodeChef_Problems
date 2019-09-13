t = int(input())
cst_final = []
for i in range(t):
    lst = list()
    x = map(int,raw_input().split())
    n = x[0]
    m = x[1]
    for j in range(n):
        y = raw_input()
        lst.append(y)
    red = 0
    for g in range(n):
        for h in range(m):
            if (g+h)%2==0:
                if lst[g][h] == 'G':
                    red += 3
            else:
                if lst[g][h] == 'R':
                    red += 5
    green = 0
    for g in range(n):
        for h in range(m):
            if (g+h)%2 == 0:
                if lst[g][h] == 'R':
                    green += 5
            else:
                if lst[g][h] == 'G':
                    green += 3

    cst_final.append(min(red,green))
for q in cst_final:
    print q