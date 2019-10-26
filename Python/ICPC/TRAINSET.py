if __name__ == '__main__':
    t = int(input())
    while t:
        n = int(input())
        dic = {}

        for i in range(n):
            inp = input().split()

            if inp[0] in dic:
                dic[inp[0]][int(inp[1])] += 1
            else:
                lst = [0, 0]
                lst[int(inp[1])] += 1
                dic[inp[0]] = lst

        cnt = 0
        for i in dic.values():
            cnt += max(i)

        print(cnt)

        t -= 1
