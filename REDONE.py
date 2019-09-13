if __name__ == '__main__':
    t = int(input())
    while t != 0:
        n = int(input())
        x = []
        val = 1
        if n >= 2:
            val = 5
        for i in range(3, n+1):
            val = val + i + val*i
            x.append(val%1000000007)

        print(val % 1000000007)
        print(x)
        t -= 1
