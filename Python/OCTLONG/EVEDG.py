import sys


class Graph:
    def __init__(self, v):
        self.v = v
        self.adj_list = [[] for _ in range(v)]

    def dfs(self, temp, v, visited):
        visited[v] = True
        temp.append(v)

        for i2 in self.adj_list[v]:
            if not visited[i2]:
                temp = self.dfs(temp, i2, visited)

        return temp

    def add_edges(self, v, w):
        self.adj_list[v].append(w)
        self.adj_list[w].append(v)

    def connected(self):
        visited = []
        c = []
        length = []
        for i2 in range(self.v):
            visited.append(False)
        for v in range(self.v):
            if not visited[v]:
                temp = []
                c.append(self.dfs(temp, v, visited))
                length.append(len(temp))

        return c, length


def get_independent(nodes):
    nds = set()
    for i1 in range(len(nodes)):
        for j1 in range(i1+1, len(nodes)):
            if list(adj_list[i1]).contains(j1) and i1 not in nds:
                nds.add(i1)

    return nds


def remove(node, graph2):
    visited = {node}

    def dfs(parent):
        nodes = []
        if parent not in visited:
            visited.add(parent)
            nodes.append(parent)
            for child in graph2[parent]:
                nodes.extend(dfs(child))
        return nodes

    subgraphs = []
    for neighbor in graph2[node]:
        if neighbor not in visited:
            subgraphs.append(dfs(neighbor))

    return subgraphs


if __name__ == '__main__':
    t = int(input())
    while t != 0:
        n, m = map(int, input().split())

        graph = Graph(n)
        deg = {}
        for i in range(m):
            x, y = map(int, input().split())
            graph.add_edges(x - 1, y - 1)

            try:
                deg[x - 1] += 1
            except Exception:
                deg[x - 1] = 1

            try:
                deg[y - 1] += 1
            except Exception:
                deg[y - 1] = 1

        cc, lengths = graph.connected()
        cc = [x1 for _, x1 in sorted(zip(lengths, cc), reverse=True)]

        adj_list = graph.adj_list
        k = 1
        ans = {}

        for i in cc:
            dup_ans = []
            if len(i) != 1:
                count = 0
                for j in i:
                    count += len(adj_list[j])

                count = count // 2

                if count & 1:
                    # odd edges
                    mn = sys.maxsize
                    ind = None
                    for j in i:
                        if deg[j] < mn and deg[j] & 1:
                            subs = remove(j, adj_list)
                            if len(subs) > 1:
                                pass
                            else:
                                mn = deg[j]
                                ind = j

                    if ind is not None:
                        deg[ind] = None
                        for j in i:
                            if deg[j] != 0 and deg[j] is not None:
                                ans[j] = k
                                dup_ans.append(k)
                    else:
                        invert = False
                        has_inverted = False
                        last = None
                        for j in i:
                            if deg[j] != 0:
                                if not invert:
                                    ans[j] = k
                                    invert = True
                                    dup_ans.append(k)
                                    last = j
                                else:
                                    ans[j] = k + 1
                                    invert = False
                                    dup_ans.append(k + 1)
                                    has_inverted = True

                        if has_inverted:
                            k += 1
                            if last is not None:
                                dup_ans.pop(-1)
                                dup_ans.append(k + 1)
                                ans[last] = k + 1
                else:
                    # even edges
                    for _ in i:
                        ans[_] = k
                        dup_ans.append(k)

            if list(dup_ans).count(k) > 1:
                k += 1

        arr = []
        lst = list(ans.values())
        mx = max(lst)

        if lst.count(mx) > 1:
            eff = False
        else:
            eff = True

        eff2 = False

        for i in range(n):
            try:
                arr.append(ans[i])
            except Exception:
                if eff:
                    arr.append(mx)
                else:
                    arr.append(mx + 1)
                    eff2 = True

        if eff2:
            print(mx + 1)
        else:
            print(mx)
        print(*arr)

        t -= 1
