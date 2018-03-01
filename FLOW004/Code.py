    t = int(input())
    lst = []
    for i in range(t):
        x = raw_input()
        a = int(x[0])
        b = int(x[-1])
        lst.append(a+b)
    for ele in lst:
        print ele 
