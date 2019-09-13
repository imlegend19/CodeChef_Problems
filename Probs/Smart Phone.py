n = int(input())
x = []
ans = []
for _ in range(n):
    a = int(input())
    x.append(a)
x.sort()
max = x[n-1]
for i in range(n-2,0,-1):
    if max < (x[i]*(n-i)):
        max = x[i]*(n-i)
print max