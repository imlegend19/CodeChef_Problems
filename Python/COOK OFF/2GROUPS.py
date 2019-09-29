if __name__ == '__main__':
    t = int(input())

    while t != 0:
        x = [int(_) for _ in input().split()]
        a = x[0]
        b = x[1]
        c = x[2]

        if a == 0:
            if b % 2 != 0 or c % 2 != 0:
                print("NO")
            else:
                print("YES")
        elif b == 0:
            if a == 1 and b == 0 and c == 1:
                print("NO")
            elif a % 2 != 0 or c % 2 != 0:
                print("NO")
            else:
                print("YES")
        elif c == 0:
            if a % 2 == 0 and b % 2 == 0:
                print("YES")
            elif (a + b) % 3 == 2 and (a % 2 == 0 or b % 2 == 0):
                print("YES")
            else:
                print("NO")
        else:
            if a % 2 != 0 and b % 2 != 0 and c % 2 != 0:
                print("YES")
            elif a % 2 == 0 and b % 2 == 0 and c % 2 == 0:
                print("YES")
            elif a % 2 != 2 and b % 2 ==0 and c % 2 != 0:
                print("YES")
            elif a % 2 != 0 and b % 2 == 0 and c % 2 == 0:
                print("NO")
            else:
                print("NO")

        t -= 1
