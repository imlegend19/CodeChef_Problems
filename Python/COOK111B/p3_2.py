import math


def nearest_power(n):
    p = int(math.log(n, 2))
    return int(pow(2, p))


if __name__ == '__main__':
    t = int(input())
    while t:
        left, right = map(int, input().split())

        nl = nearest_power(left)
        nr = nearest_power(right)

        if left <= nr <= right:
            if nr - 1 > left:
                print(nr | nr - 1)
            else:
                print(nr | nr + 1)
        else:
            lbin = bin(left)[2:]
            rbin = bin(right)[2:]

            s1 = ''
            it = 0
            for i, j in zip(lbin, rbin):
                if i == j:
                    s1 += i
                else:
                    vall = "".join(lbin[it:])
                    valr = "".join(rbin[it:])

                    break

                it += 1

            nr = nearest_power(int(valr, 2))
            s1 += str(bin(nr)[2:])

            print(int(s1, 2) | int(s1, 2) - 1)

        t -= 1
