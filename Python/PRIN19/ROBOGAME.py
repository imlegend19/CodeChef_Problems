if __name__ == '__main__':
    t = int(input())
    while t:
        s = list(input())
        f = 0
        for i in range(0, len(s)):
            if s[i] != '.':
                n = int(s[i])
                for x in range(i - n, i + n + 1):
                    if 0 <= x < len(s) and x != i:
                        if s[x] == '.':
                            s[x] = '0'
                        else:
                            f = 1
                            print('unsafe')
                            break
                    if f == 1:
                        break
            if f == 1:
                break

        if f == 0:
            print('safe')

        t -= 1
