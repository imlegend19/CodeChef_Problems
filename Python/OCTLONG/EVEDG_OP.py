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


if __name__ == '__main__':
    t = int(input())
    while t != 0:
        edges = set()
        n, m = map(int, input().split())
        graph = Graph(n)

        deg = {}
        for i in range(m):
            x, y = map(int, input().split())
            graph.add_edges(x - 1, y - 1)
            edges.add((x-1, y-1))

            try:
                deg[x - 1] += 1
            except Exception:
                deg[x - 1] = 1

            try:
                deg[y - 1] += 1
            except Exception:
                deg[y - 1] = 1

        cc, lengths = graph.connected()
        cc = [x1 for _, x1 in sorted(zip(lengths, cc))]

        adj_list = graph.adj_list

        ans = {}
        for i in cc:
            if len(i) == 1:
                pass
            else:
                count = 0
                for j in i:
                    count += len(adj_list[j])

                count = count // 2

                if count & 1:
                    mn = sys.maxsize
                    ind = None
                    for j in i:
                        if deg[j] < mn and deg[j] & 1:
                            mn = deg[j]
                            ind = j

                    if ind is not None:
                        for j in i:
                            if j == ind:
                                ans[j] = 2
                            else:
                                ans[j] = 1
                    else:
                        for j in range(len(i) - 2):
                            ans[i[j]] = 1
                        ans[i[-1]] = 2
                        ans[i[-2]] = 3
                else:
                    for j in i:
                        ans[j] = 1

        arr = []
        k = max(ans.values())
        for i in range(n):
            try:
                arr.append(ans[i])
            except Exception:
                arr.append(k)

        print(k)
        print(*arr)

        t -= 1
