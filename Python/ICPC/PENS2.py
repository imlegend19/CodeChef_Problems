if __name__ == '__main__':
    t = int(input())
    while t:
        n, p = map(int, input().split())
        s = list(input())
        master = set(s)

        dic = {}
        for i in range(p):
            s1 = set(input())
            sc = len(master.intersection(s1))
            for j in s1:
                try:
                    val = dic[j]
                    if val[1] < sc:
                        val = [i+1, sc]
                        dic[j] = val
                except Exception:
                    dic[j] = [i+1, sc]

        for i in s:
            print(dic[i][0], end=" ")

        print()

        t -= 1
