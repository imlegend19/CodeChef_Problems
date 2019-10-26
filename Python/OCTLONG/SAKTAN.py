def print_matrix(matrix):
    print(get_odd(matrix))
    for p in matrix:
        print(*p)


def get_odd(matrix):
    to = 0
    for i1 in matrix:
        for j1 in i1:
            if j1 % 2 != 0:
                to += 1

    return to


if __name__ == '__main__':
    t = int(input())
    while t != 0:
        n, m, q = map(int, input().split())

        mat = []
        for j in range(n):
            mat.append([0 for _ in range(m)])

        for i in range(q):
            x, y = map(int, input().split())
            for j in range(m):
                mat[x-1][j] += 1

            for j in range(n):
                mat[j][y-1] += 1

            print_matrix(mat)

        tot = 0
        for i in mat:
            for j in i:
                if j % 2 != 0:
                    tot += 1

        print(tot)
        t -= 1

#1 4 4 3 1 1 1 3 2 3
# 6
#1 6 6 3 1 3 2 4 1 5
# 18