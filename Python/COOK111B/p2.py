import math

if __name__ == '__main__':
    t = int(input())
    while t:
        n = input()

        if n == 10 or n == 20:
            print("Yes")
        else:
            cnt = 0
            for i in range(len(n) - 1, -1, -1):
                if n[i] == '0':
                    cnt += 1
                else:
                    break

            if cnt == 0 :
                print("No")
            else:
                n = n.strip("0")
                l2 = math.log2(int(n))

                if l2 % 1 == 0:
                    l2 = int(l2)
                    if l2 <= cnt:
                        print("Yes")
                    else:
                        print("No")
                else:
                    print("No")

        t -= 1
