if __name__ == '__main__':
    t = int(input())

    while t != 0:
        n, k = map(int, input().split())
        arr = [int(_) for _ in input().split()]

        for i in range(k):
            arr[i % n] = (arr[i % n]) ^ (arr[n - (i % n) - 1])
            print(i+1, ":", *arr)

        t -= 1
