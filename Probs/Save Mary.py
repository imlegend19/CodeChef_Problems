def Murder(n, k):
    if (n == 1):
        return 1
    else:
        x = (Murder(n - 1, k) + k-1) % n + 1
        if x!=None:
            return x
        else:
            return -1

ans = []

t = int(input())
for _ in range(t):
    n = int(input())
    k = int(input())
    ans.append(Murder(n, k))

for e in ans:
    print(e)