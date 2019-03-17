a = map(float,raw_input().split())
x = a[0]
y = a[1]
c = y-x-0.5
if(c>=0 and (x%5==0)):
    print c
else:
    print y
