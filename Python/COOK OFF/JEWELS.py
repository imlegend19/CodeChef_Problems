if __name__ == '__main__':
    t = int(input())

    while t != 0:
        inp = [int(_) for _ in input().split()]
        n = inp[0]
        m = inp[1]

        cost = [int(_) for _ in input().split()]

        prevented = False
        max_cst = max(cost)
        stolen = []

        for i in range(m):
            l, r = raw_input().split()
            avail = cost[l:r+1]
            avail.sort(reverse=True)

            for j in avail:
                if j in stolen:
                    

        t -= 1
