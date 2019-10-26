if __name__ == '__main__':
    t = int(input())
    while t:
        n, p = map(int, input().split())
        s = list(input())
        master = set(s)

        dic = {}
        scores = []
        nums = []
        mx = -1
        ind = None
        for i in range(p):
            s1 = set(input())
            sc = len(master.intersection(s1))
            scores.append(sc)
            nums.append(i)
            dic[i] = s1
            if sc > mx:
                mx = sc
                ind = i

        if mx >= len(master):
            for i in range(n):
                print(ind+1, end=" ")
        else:
            nums = [x for _, x in sorted(zip(scores, nums), reverse=True)]

            ans = []
            for i in s:
                for j in nums:
                    if i in dic[j]:
                        ans.append(j+1)
                        break

            str1 = ' '.join(map(str, ans))
            print(str1)

        t -= 1
