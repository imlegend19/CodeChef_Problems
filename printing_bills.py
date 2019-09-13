if __name__ == '__main__':
    n = int(input())
    prices = []
    strings = []
    lower_strings = []

    dict_price = {}

    total = 0

    for i in range(n):

        lst = [_ for _ in input().split()]
        s = lst[0]
        p = float(lst[1])
        d = float(lst[2])

        strings.append(s)
        lower_strings.append(s.lower())
        x = round(float(p-(p*d)/100.0), 2)
        prices.append(x)
        total += float(x)

        if x in dict_price:
            dict_price[x] += 1
        else:
            dict_price[x] = 1

    prices, strings, lower_strings = (list(t) for t in zip(*sorted(zip(prices, strings, lower_strings), reverse=True)))

    for i in dict_price.keys():
        if dict_price[i] > 1:
            set_strings = []
            index = prices.index(i)
            t_index = index
            for j in range(dict_price[i]):
                set_strings.append(str(strings[t_index]).upper())
                t_index += 1

            if set_strings == set_strings.sort():
                pass
            else:
                set_strings.sort()
                for j in range(len(set_strings)):
                    if set_strings[j] != str(strings[index]).upper():
                        ik = lower_strings.index(set_strings[j].lower())
                        temp = strings[index]
                        strings[index] = strings[ik]
                        strings[ik] = temp

                        temp = prices[index]
                        prices[index] = prices[ik]
                        prices[ik] = prices[index]
                    index += 1

    for i in range(n):
        print(strings[i] + ' ' + '%.2f' % float(prices[i]))

    print('Total' + ' ' + '%.2f' % float(total))
