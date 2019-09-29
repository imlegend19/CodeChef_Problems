def print_duplicates(arr):
    dict = {}

    for ele in arr:
        try:
            dict[ele] += 1
        except Exception:
            dict[ele] = 1

    return dict


if __name__ == '__main__':
    t = int(input())
    while t != 0:
        n = int(input())
        x = [int(_) for _ in input().split()]

        if n % 2 == 0:
            print(-1)
        else:
            x1 = set()
            x2 = set()
            for i in x:
                if i in x1:
                    x2.add(i)
                else:
                    x1.add(i)

            y = list(x1 - x2)
            print(y[0])

        t -= 1
