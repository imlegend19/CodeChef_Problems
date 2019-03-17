import string
t = int(input())
ans = []
for _ in range(t):
    x = raw_input()
    alpha = list(string.ascii_lowercase)
    str = []
    alpha2 = list(string.ascii_lowercase)
    alpha2 = alpha2[::-1]
    for i in range(len(x)):
        a = alpha.index(x[i])
        str.append(alpha2[a])
    str = ''.join(str)
    ans.append(str)
for e in ans:
    print e