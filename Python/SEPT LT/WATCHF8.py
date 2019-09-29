if __name__ == '__main__':
    t = int(input())
    while t != 0:
        n = int(input())
        cs = [0, 0]
        for i in range(n):
            tp, a, b = map(int, input().split())
            if a < min(cs) or b < min(cs):
                print('NO')
            elif tp == 1:
                cs = [a, b]
                print('YES')
            else:
                if a == b:
                    print('YES')
                    cs = [a, b]
                elif min([a, b]) < max(cs):
                    print('YES')
                    if cs[0] < cs[1]:
                        cs = [a, b]
                    else:
                        cs = [b, a]
                else:
                    print('NO')
        t -= 1
