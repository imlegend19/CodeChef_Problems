t = int(input())
ans = []
for _ in range(t):
    n, w = map(int, input().split())
    s = ''
    if w > (n*2):
        ans.append(0)
    else:
        if w == 0:
            s += '9'
            s += '0' * (n - 2)
        elif w == 1:
            s += '8'
            s += '0' * (n - 2)
        elif w == 2:
            s += '7'
            s += '0' * (n - 2)
        elif w == 3:
            s += '6'
            s += '0' * (n - 2)
        elif w == 4:
            s += '5'
            s += '0' * (n - 2)
        elif w == 5:
            s += '4'
            s += '0' * (n - 2)
        elif w == 6:
            s += '3'
            s += '0' * (n - 2)
        elif w == 7:
            s += '2'
            s += '0' * (n - 2)
        elif w == 8:
            s += '1'
            s += '0' * (n - 2)
        else:
            ans.append(0)
        if s != '':
            ans.append(int(s)%1000000007)

for e in ans:
    print(e)