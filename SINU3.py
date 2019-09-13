ans = []


def find_root(i):
    while i != root[i]:
        root[i] == root[root[i]]
        i = root[i]
    return i


def delete_edge(u):
    root[u] = u


def union(u, v):
    root_u = find_root(u)
    root_v = find_root(v)
    if root_u == root_v: return
    root[u] = v


def find_pairs():
    d = {}
    c = 0
    for i, j in enumerate(root):
        r = find_root(i)
        if r not in d:
            d[r] = [i]
        else:
            d[r].append(i)

    for val in d.values():
        if len(val) == 1: continue
        for x in range(len(val)):
            for y in range(x + 1, len(val)):
                if abs(arr[val[x]] - arr[val[y]]) <= e:
                    c += 1

    return c


edge_list = []

n, e = [int(i) for i in input().split()]
arr = [int(i) for i in input().split()]

root = [i for i in range(n)]

for _ in range(n - 1):
    u, v = [int(i) for i in input().split()]
    edge_list.append((u - 1, v - 1))
    union(u - 1, v - 1)

for _ in range(n - 1):
    u, v = edge_list[int(input()) - 1]
    delete_edge(u)
    ans.append(find_pairs())


for e in ans:
    print(e)
