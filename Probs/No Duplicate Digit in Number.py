def anydup(thelist):
    seen = list()
    flag = 0
    for x in thelist:
        if x in seen:
            flag = 1
            break
        else:
            seen.append(x)
    if flag == 0:
        return 1
    else:
        return 0


lst = [x for x in range(5000, 10001)]
count = 0
for i in lst:
    j = list(str(i))
    x = anydup(j)
    if x == 1:
        count += 1
print(count)




