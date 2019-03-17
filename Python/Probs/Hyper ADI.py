t = int(input())
ans = []
for _ in range(t):
    x = raw_input()
    a = []
    a_count = x.count('a')
    e_count = x.count('e')
    i_count = x.count('i')
    o_count = x.count('o')
    u_count = x.count('u')
    if (a_count and u_count and i_count and o_count and e_count)>0:
        ans.append(x)
    else:
        continue
for e in ans:
    print e