def __gcd(a, b):
    if a == 0 or b == 0:
        return 0

    if a == b:
        return a

    if a > b:
        return __gcd(a - b, b)

    return __gcd(a, b - a)


if __name__ == '__main__':
    t = int(input())
    while t:
        n, k = map(int, input().split())
        rows = set()
        cols = set()
        for _ in range(k):
            r, c = map(int, input().split())
            rows.add(r)
            cols.add(c)

        no = (n - len(cols)) * (n - len(rows))
        if no == 0:
            print("Impossible")
        else:
            if __gcd(no, n*n) == 1:
                print(no, n*n)
            else:
                print("Impossible")

        t -= 1
