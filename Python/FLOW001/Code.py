    t = int(input())
    lst = []
    for i in range(t):
        x = map(int,raw_input().split())
        a = x[0]
        b = x[1]
        lst.append(int(a+b))
    for j in lst:
        print j 
