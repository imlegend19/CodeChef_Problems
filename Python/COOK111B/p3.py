if __name__ == '__main__':
    t = int(input())
    while t:
        left, right = map(int, input().split())

        left = bin(left)[2:]
        right = bin(right)[2:]

        limit = len(left)
        flag = False
        num = ''
        for i in range(len(right)):
            if not flag:
                if right[i] == '1':
                    if i >= limit - 1:
                        num += left[i - limit + 1]
                    else:
                        num += '0'
                else:
                    num += '1'
                    flag = True
            else:
                if right[i] == '1':
                    num += '0'
                else:
                    num += '1'

        num = int('0b' + num)
        right = int('0b' + right)

        print(num | right)

        t -= 1
