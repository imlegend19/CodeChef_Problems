if __name__ == '__main__':
    t = int(input())
    while t != 0:
        n, k = map(int, input().split())
        graph = {}
        for i in range(n-1):
            x, y = map(int, input().split())
            if x in graph:
                graph[x].append(y)
                try:
                    graph[y].append(x)
                except Exception:
                    graph[y] = [x]
            elif y in graph:
                graph[y].append(x)
                try:
                    graph[x].append(y)
                except Exception:
                    graph[x] = [y]
            else:
                graph[x] = [y]

        print(graph)

        t -= 1
