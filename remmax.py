if __name__ == '__main__':
    t = int(input())
    while t != 0:
        n = input()

        if n == n[::-1]:
            print(n)
        else:
            if int(n) < 20:
                print(n)
            else:
                x = int(n) % 10
                num = int(n) - x - 1
                print(num)

        t -= 1
