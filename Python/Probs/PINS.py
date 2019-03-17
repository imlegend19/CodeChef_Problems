t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    # n = len(arr)
    # m = divisor
    arr = [int(x) for x in input().split()]


def subArray(arr, n):
    # Pick starting point
    for i in range(0, n):

        # Pick ending point
        for j in range(i, n):

            # Print subarray between
            # current starting
            # and ending points
            s = ''
            for k in range(i, j + 1):
                if k % m == 0:
                    s += str(arr[k])

