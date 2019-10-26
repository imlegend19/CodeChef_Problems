if __name__ == '__main__':
    t = int(input())
    while t != 0:
        n = int(input())
        if n & 1 and n != 1:
            print("YES")
            mrk = (n-1)/2
            x = [0]
            for i in range(1, n):
                if mrk == 0:
                    x.append(0)
                else:
                    x.append(1)
                    mrk -= 1

            print(''.join(str(_) for _ in x))
            for i in range(n-1):
                x = x[-1:] + x[:-1]
                print(''.join(str(_) for _ in x))
        else:
            print("NO")

        t -= 1
