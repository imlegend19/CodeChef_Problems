    t = int(input())
    lst = []
    for i in range(t):
        x = raw_input()
        y = x[::-1]
        lst.append(int(y))
    for ele in lst:
        print ele 
