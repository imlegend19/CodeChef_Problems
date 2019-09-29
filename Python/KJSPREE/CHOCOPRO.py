def solution(a, b, n):
    i = 1
    while i * a <= n:
        if (n - (i * a)) % b == 0 and (int((n - (i * a)) / b)) != 0:
            return i, int((n - (i * a)) / b)
        i = i + 1

    return None


if __name__ == '__main__':
    t = int(input())
    while t != 0:
        n, x = map(int, input().split())
        sol = solution(x, int(x*(x-1)/2), n)
        if sol is not None:
            print('Y', sol[0])
        else:
            print('N')

        t -= 1
