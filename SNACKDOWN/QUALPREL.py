t = int(input())
ans = []
for i in range(t):
    n, k = map(int, input().split())
    s = [int(x) for x in input().split()]
    s.sort(reverse=True)
    d = s[k-1]
    cnt = 0
    for j in s:
        if j > d or j == d:
            cnt += 1
    ans.append(cnt)

for e in ans:
    print(e)
