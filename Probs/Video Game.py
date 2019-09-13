n,h = map(int,raw_input().split())
hl = map(int,raw_input().split())
c = map(int,raw_input().split())
pos = 0
i = 0
p = 0
d = 1
while (c[i]!=0):
    if c[i]==1:
        if (pos != 0):
            pos -= 1
    if c[i]==2:
        if (pos != n-1):
            pos += 1
    if c[i]==3:
        if p==1 and d==0:
            p=1
        elif (d!=0):
            if hl[pos]!=0:
                hl[pos]=hl[pos]-1
                p=1
            else:
                p=0
        else:
            p=0
    if c[i]==4:
        if p!=0:
            if (hl[pos]!=h):
                hl[pos]=hl[pos]+1
                d=1
            else:
                d=0
        else:
            d=0
    i+=1
print(" ".join(map(str,hl)))
