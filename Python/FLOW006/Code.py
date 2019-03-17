    t = int(input())
    last = []
    for i in range(t):
        x = raw_input()
        sum = 0
        for j in range(len(x)):
            sum += int(x[j])
        last.append(sum)
    for ele in last:
        print ele 
