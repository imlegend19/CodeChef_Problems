t = int(input())
ans = []
for _ in range(t):
    n = int(input())
    x = map(int,raw_input().split())
    if (len({}.fromkeys(x)) == len(x))==True:
        ans.append(0)
    else:
        count = 0
        new_array = dict.fromkeys(x).keys()
        count = len(x) - len(new_array)
        ans.append(count)
for e in ans:
    print e