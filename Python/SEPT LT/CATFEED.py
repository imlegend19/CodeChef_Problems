if __name__ == '__main__':
    t = int(input())

    while t != 0:
        n, m = map(int, input().split())
        arr = [_ for _ in input().split()]

        fair = True
        for i in range(0, m, n):
            s = arr[i:i+n]
            if len(s) == len(set(s)):
                pass
            else:
                fair = False
                break

        if fair:
            print("YES")
        else:
            print("NO")

        t -= 1

