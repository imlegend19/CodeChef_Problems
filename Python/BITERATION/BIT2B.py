if __name__ == '__main__':
    t = int(input())
    while t != 0:
        n = int(input())
        cost = [int(_) for _ in input().split()]
        x = int(input())

        boxes = [0, 0]

        j = 0
        for i in range(n-1, -1, -1):
            if i == j:
                c = cost[j]
                if c != 0:
                    if boxes[0] >= boxes[1]:
                        boxes[0] += 1
                    else:
                        boxes[1] += 1

                break

            c = cost[i]
            eff = c * x

            cost[i] -= c
            boxes[1] += 1

            while eff != 0 and i != j:
                if eff >= cost[j]:
                    eff -= cost[j]
                    cost[j] = 0
                    j += 1
                    boxes[0] += 1
                else:
                    cost[j] -= eff
                    eff = 0

                    if j == i - 1:
                        boxes[0] += 1
                        j = i

            if i == j:
                break

        print(boxes[0], boxes[1])

        t -= 1
