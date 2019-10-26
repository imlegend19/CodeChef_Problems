if __name__ == '__main__':
    t = int(input())
    while t:
        n = int(input())
        arr = [int(_) for _ in input().split()]

        if arr.index(max(arr)) < arr.index(min(arr)):
            print(max(arr), min(arr))
        else:
            print(min(arr), max(arr))

        t -= 1
