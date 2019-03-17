import math
t = int(input())
ans = []
for _ in range(t):
    a = map(int,raw_input().split())
    n = a[0]
    h = a[1]
    x = map(int,raw_input().split())
    h_count = 0
    k = min(x)
    while(h>=h_count):
        for i in x:
            if i<=k:
                h_count += 1
            else:
                r = math.ceil(float(i) / k)
                h_count += r
        if h<h_count:
            h_count = 0
            k += 1
        else:
            break
    ans.append(k)
for e in ans:
    print e