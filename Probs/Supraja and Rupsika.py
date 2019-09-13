t = int(input())
ans = []
def all_same(items):
    return all(x == items[0] for x in items)
for _ in range(t):
    a = []
    n,m = map(int,raw_input().split())
    matrix = []
    for i in range(0,n):
        x = raw_input()
        matrix.append(x)
    horiz_count = 0
    vert_count = 0
    for k in range(n):
        b = []
        b[:] = []
        for l in matrix[k]:
            b.append(l)
        b1 = []
        b1[:] = []
        for l1 in b:
            b1.append(b.count(l1))
        if horiz_count<int(max(b1)):
            horiz_count += int(max(b1))

    for k in range(m):
        c = []
        c1 = []
        c[:]=[]
        for p in range(n):
            c1.append(matrix[p][k])
        if all_same(c1)==True:
            c.append(len(c1))
        else:
            for o in c1:
                c.append(c1.count(o))
        if vert_count<int(max(c)):
            vert_count += max(c)
    ans.append(max(horiz_count,vert_count))
for e in ans:
    print e
