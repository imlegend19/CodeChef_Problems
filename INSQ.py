def ncr(n1, r):
    return int((fact(n1) / (fact(r)
                            * fact(n1 - r))))


# Returns factorial of n
def fact(n1):
    res = 1

    for i1 in range(2, n1 + 1):
        res = res * i1

    return res


if __name__ == '__main__':
    t = int(input())
    while t != 0:
        n, k = map(int, input().split())

        arr = [int(_) for _ in input().split()]
        arr.sort()

        ele = arr[k - 1]
        occ = 0

        for i in range(k, n):
            if arr[i] == ele:
                occ += 1
            else:
                break

        main_occ = 0
        for i in range(k):
            if arr[i] == ele:
                main_occ += 1

        print(ncr(main_occ + occ, main_occ))

        t -= 1
