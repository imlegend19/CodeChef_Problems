if __name__ == '__main__':
    t = int(input())
    it = 1
    while t != 0:
        n, s = map(int, input().split())
        skills = []
        for i in range(n):
            inp = [int(_) for _ in input().split()]
            inp.pop(0)
            skills.append(inp)

        pairs = set()
        for i in range(len(skills)):
            for j in range(len(skills)):
                if j != i:
                    if set(skills[j]).intersection(skills[i]) != set(skills[j]):
                        pairs.add((i, j))

        print("Case #" + str(it) + ": " + str(len(pairs)))
        it += 1

        t -= 1
