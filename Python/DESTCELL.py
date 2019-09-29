if __name__ == '__main__':
    t = int(input())
    while t != 0:
        n, m = map(int, input().split())
        arr = []
        for k in range(n*m):
            cnt = 0
            for i in range(0, n*m, k+1):
                cnt += 1
            arr.append(cnt)

        print(*arr)
        t -= 1
