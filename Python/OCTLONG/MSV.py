def evaluate(nm, bs):
    numb = 0
    iterator = len(nm) - 1
    for char in nm:
        try:
            pop = int(char)
        except Exception:
            pop = ord(char) - 55

        numb += pop * pow(bs, iterator)
        iterator -= 1

    return numb


if __name__ == '__main__':
    t = int(input())

    while t != 0:
        n = int(input())
        result = None
        pre = True

        decimal = []
        for i in range(n):
            inp = [_ for _ in input().split()]
            b = int(inp[0])
            s = inp[1]
            end = 37

            if b != -1:
                if result is not None:
                    num = evaluate(s, b)
                    if num < 36:
                        end = num + 1
                    if num != result:
                        pre = False
                else:
                    result = evaluate(s, b)
            else:
                if s.isdigit():
                    start = int(max(s)) + 1
                    if start < 2:
                        start = 2
                else:
                    start = ord(max(s)) - 55

                lst = []
                for j in range(start, end):
                    ev = evaluate(s, j)
                    if ev < 36:
                        end = ev + 1
                    if ev < pow(10, 12):
                        lst.append(ev)

                if len(lst) != 0:
                    decimal.append(lst)
                else:
                    pre = False

        if pre:
            if result is not None:
                valid = True
                for i in decimal:
                    if result not in i:
                        valid = False
                        break

                if valid:
                    if result < pow(10, 12):
                        print(result)
                    else:
                        print(-1)
                else:
                    print(-1)
            else:
                try:
                    minimal = set(decimal[0]).intersection(*decimal)
                except ValueError:
                    minimal = set()

                try:
                    mn = min(minimal)
                    if mn > pow(10, 12):
                        print(-1)
                    else:
                        print(mn)
                except Exception:
                    print(-1)
        else:
            print(-1)

        t -= 1
