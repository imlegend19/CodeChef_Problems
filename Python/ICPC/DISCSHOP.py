if __name__ == '__main__':
    t = int(input())
    while t:
        n = list(str(int(input())))

        if '0' in n:
            sub = n[:n.index('0')]
            n.remove(max(sub))

        else:
            sub = []
            mx = '-1'
            for i in n:
                if i > mx:
                    sub.append(i)
                    mx = i
                else:
                    break
            n.remove(max(sub))

        lst = ''.join(map(str, n))
        print(int(lst))

        t -= 1
