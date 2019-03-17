t = int(input())
ans = []
for _ in range(t):
    x = int(input())
    i = 2
    factors = []
    while i * i <= x:
        if x % i:
            i += 1
        else:
            x //= i
            factors.append(i)
    if x > 1:
        factors.append(x)
    a = []
    for i in factors:
        if i not in a:
            a.append(i)
        else:
            continue
    ans.append(a)

for e in ans:
    print(" ".join(map(str, e)))