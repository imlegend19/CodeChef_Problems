    t = int(input())
    lst = []
    for i in range(t):
        x = int(input())
        fact = 1
        for i in range(1,x+1):
            fact = fact*i
        lst.append(fact)
    for j in lst:
        print j 
