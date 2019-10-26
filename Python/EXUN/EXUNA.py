if __name__ == '__main__':
    t = int(input())
    while t != 0:
        n = int(input())
        x = [int(_) for _ in input().split()]
        x.sort()
        mod = None
        for i in x:
            if mod is None:
                mod = i
            else:
                mod %= i

        print(mod)
        t -= 1
