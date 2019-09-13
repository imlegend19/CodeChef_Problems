t = int(input())
ans = []
for i in range(t):
    n = int(input())
    x = [int(x) for x in input().split()]
    days = 0
    total_cnt = 0
    index = 0
    while True:
        cnt = 0
        for j in range(index + 1):
            total_cnt += x[j]
            cnt += x[j]
        days += 1
        index += cnt

        if total_cnt >= len(x) - 1:
            break
    ans.append(days)

for e in ans:
    print(e)
