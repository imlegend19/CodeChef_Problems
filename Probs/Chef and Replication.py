t = int(input())
ans = []
for _ in range(t):
    n, k = map(int, input().split())
    n2 = [int(x) for x in input().split()]
    a = []
    for i in n2:
        if n2.count(i) == k:
            if i not in a:
                a.append(i)
    if len(a) != 0:
        ans.append(sum(a))
    else:
        ans.append(-1)
    a[:] = []
for e in ans:
    print(e)