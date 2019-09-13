t = int(input())
lst0 = []
z = []
b1 = []
lst1 = []
t2 = []
for q in range(t):
    x = map(int, raw_input().split())
    a = x[0]
    b = x[1]
    b1.append(b)
    lst2 = []
    y = map(int, raw_input().split())
    z.append(y)
    for l in y:
        if l%b == 0:
            lst2.append(l)
    if len(lst2) != 0:
        target = max(lst2)
        lst1.append([target])
        t2.append(target)
    else:
        target = 0
        lst1.append([target])
        t2.append(target)

for k in range(len(t2)):
    for i in range(len(z)):
        if t2[k] in z[i]:
            z[i].remove(t2[k])
        for p in z[i]:
             if p<t2[k]:
                pair = t2[k] - p
                if pair in z[i]:
                    if pair != p:
                        lst1[i].append([pair,p])
                        z[i].remove(pair)
                        z[i].remove(p)

new_array = list()
nums = list()
for i in b1:
    if (i not in nums):
        new_array.append(i)
        nums.append(i)

o = 0

for p in range(len(lst1)):
    if o in lst1[p]:
        lst1[p].remove(o)
    if (len(lst1[p]) == new_array[0]) and (new_array[0] != 1):
        lst0.append('yes')
    elif new_array[0] == 1:
        lst0.append('yes')
    else:
        lst0.append('no')

for e in lst0:
    print e