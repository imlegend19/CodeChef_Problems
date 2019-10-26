if __name__ == '__main__':
    for _ in range(int(input())):
        n, k = map(int, input().split())
        arr = [int(x) for x in input().split()]
        arr.sort()

        b = []
        result = 0
        for x in arr[:-1]:
            if x > k:
                b.append(x - k)
            else:
                result = result + x

        result = result + len(b) * k + arr[n - 1]

        if len(b) == 0:
            print(result)
            continue

        mid = sum(b[:-1])

        if mid <= b[len(b) - 1]:
            diff = b[len(b) - 1] - mid
            result = result - diff
        else:
            mid = sum(b)
            if mid % 2 == 1:
                result -= 1

        print(result)
