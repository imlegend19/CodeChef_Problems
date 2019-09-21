if __name__ == '__main__':
    t = int(input())
    while t != 0:
        n = int(input())
        lst = [int(_) for _ in input().split()]

        occ = {}
        for i in lst:
            if i in occ:
                val = occ[i] + 1
                occ[i] = val
            else:
                occ[i] = 1

        b = []
        prev = None
        prev_num = None
        for i in range(n):
            if i == 0:
                item = lst[i]
                x = occ[item]
                b.append(n - x)
                prev = item
                prev_num = n - x
            else:
                item = lst[i]
                x = occ[item]
                if lst[i] == prev:
                    b.append(prev_num)
                else:
                    b.append(n - x - i)
                    prev = item
                    prev_num = n - x - i

        print(" ".join(list(map(str, b))))

        t -= 1
