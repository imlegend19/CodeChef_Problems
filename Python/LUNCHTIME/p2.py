def getSum(BITree, index):
    sum = 0
    while (index > 0):
        sum += BITree[index]
        index -= index & (-index)

    return sum


def updateBIT(BITree, n, index, val):
    while (index <= n):
        BITree[index] += val
        index += index & (-index)


def getInvCount(arr, n):
    invcount = 0
    maxElement = max(arr)

    BIT = [0] * (maxElement + 1)
    for i in range(1, maxElement + 1):
        BIT[i] = 0
    for i in range(n - 1, -1, -1):
        invcount += getSum(BIT, arr[i] - 1)
        updateBIT(BIT, maxElement, arr[i], 1)
    return invcount


if __name__ == '__main__':
    t = int(input())
    while t:
        n = int(input())

        arr = [int(_) for _ in input().split()]
        res = getInvCount(arr, n)
        print(res)

        for q in range(1, 10):
            arr = arr * q
            res = getInvCount(arr, n*q)
            print(res)

        t -= 1
