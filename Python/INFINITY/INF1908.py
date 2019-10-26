if __name__ == '__main__':
    t = int(input())
    while t:
        n, k = map(int, input().split())
        k %= 10

        temp = (n + k) % 10

        n = list(str(n))
        n[-1] = str(temp)
        n = "".join(n)

        print(n)

        t -= 1
