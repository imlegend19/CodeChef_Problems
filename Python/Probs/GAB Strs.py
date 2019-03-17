t = int(input())
ans = []
for _ in range(t):
    num = int(input())
    x = int(input())
    y = str(x)
    flip = 0
    for i in range(0,len(y)):
        if ((i+2)<len(y)):
            if (y[i]=='0' and y[i+1]=='1' and y[i+2]=='0'):
                y.replace(y[i+2],'1')
                flip += 1
    ans.append(flip)

for e in ans:
    print e
