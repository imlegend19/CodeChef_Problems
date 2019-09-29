if __name__ == '__main__':
    t = int(input())

    p = {'1': 2, '0': 6, '2': 5, '3': 5, '4': 4, '5': 5, '6': 6, '7': 3, '8': 7, '9': 6}

    while t != 0:
        x = [int(_) for _ in input().split()]
        a = x[0]
        b = x[1]

        c = list(str(a + b))

        cost = 0
        for i in c:
            cost += p[i]

        print(cost)

        t -= 1
