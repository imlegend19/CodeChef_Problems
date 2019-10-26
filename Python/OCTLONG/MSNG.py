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
        max_valid = None

        decimal = []
        for i in range(n):
            inp = [_ for _ in input().split()]
            b = int(inp[0])
            s = inp[1]

            if b != -1:
                if result is not None:
                    num = evaluate(s, b)
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
                    start = ord(max(s)) - 54

                lst = []
                for j in range(start, 37):
                    ev = evaluate(s, j)
                    if max_valid is not None:
                        if ev > max_valid:
                            break
                    if ev <= pow(10, 12):
                        lst.append(ev)
                    else:
                        break

                try:
                    if max_valid is None:
                        max_valid = max(lst)
                    else:
                        if max(lst) < max_valid:
                            max_valid = max(lst)
                except Exception:
                    pre = False

                decimal.append(lst)

        if pre:
            if result is not None:
                valid = True
                for i in decimal:
                    if result not in i:
                        valid = False
                        break

                if valid:
                    if result <= pow(10, 12):
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
                except ValueError:
                    print(-1)
        else:
            print(-1)

        t -= 1
