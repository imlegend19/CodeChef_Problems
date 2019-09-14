def ncr(n, r):
    return (fact(n) / (fact(r)
                       * fact(n - r)))


def fact(n1):
    res = 1

    for i in range(2, n1 + 1):
        res = res * i

    return res


if __name__ == '__main__':
    t = int(input())
    while t != 0:
        n, m = map(int, input().split())
        x = ncr(n, 2) + n

        if m > x:
            print(-1)
        elif m == x:
            print(n)
        elif m >= x - n:
            print(n - 1)
        elif m >= ncr(n-1, 2) + 2:
            print(m - n - 1)
        elif m >= n:
            print(2)
        elif m < n:
            print(1)
        else:
            print(-1)

        t -= 1
