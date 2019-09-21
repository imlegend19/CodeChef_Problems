ops = ['|', '&', '^']


def is_operand(c):
    if c in ops:
        return True
    else:
        return False


def value(c):
    return int(c)


def evaluate(exp):
    len1 = len(exp)

    if len1 == 0:
        return -1

    res = value(exp[0])
    for i in range(0, len1, 2):
        opr = exp[i]
        opd = exp[i + 1]

        if not is_operand(opd):
            return -1

        if opr == '|':
            res |= value(opd)
        elif opr == '^':
            res ^= int(value(opd))
        elif opr == '&':
            res &= int(value(opd))

    return res


if __name__ == '__main__':
    t = int(input())
    while t != 0:
        st = list(input())

        lst = []

        num_pre = False
        num = ""
        for i in st:
            if i in ops:
                num_pre = False
                lst.append(num)
                num = ""
                lst.append(i)
            else:
                num += i

        print(evaluate(lst))

        t -= 1



