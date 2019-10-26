if __name__ == '__main__':
    t = int(input())
    while t != 0:
        n, m, q = map(int, input().split())

        rcnt = [0 for _ in range(n)]
        ccnt = [0 for _ in range(m)]

        pairs = {}
        for i in range(q):
            r, c = map(int, input().split())

        t -= 1
