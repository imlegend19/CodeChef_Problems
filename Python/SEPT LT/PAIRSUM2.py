def are_consecutive(arr, n1):
    if n1 < 1:
        return False

    mn = getMin(arr, n1)
    mx = getMax(arr, n1)

    if mx - mn + 1 == n1:
        for i in range(n1):
            if arr[i] < 0:
                j = -arr[i] - mn
            else:
                j = arr[i] - mn

            if arr[j] > 0:
                arr[j] = -arr[j]
            else:
                return False

        return True

    return False


def get_min(arr, n1):
    mn = arr[0]
    for i1 in range(1, n1):
        if arr[i1] < mn:
            mn = arr[i1]
    return mn


def get_max(arr, n1):
    mx = arr[0]
    for i1 in range(1, n1):
        if arr[i1] > mx:
            mx = arr[i1]
    return mx


if __name__ == '__main__':
    t = int(input())
    n, q = map(int, input().split())

    b = [int(_) for _ in range(n - 1)]

    for i in range(q):
        p, q = main(int, input().split())
        if are_consecutive([p, q], 2):
            print(b[min([p, q]) - 1])
        else:
            pass
