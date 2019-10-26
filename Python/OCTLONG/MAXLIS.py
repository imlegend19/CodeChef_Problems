if __name__ == '__main__':
    n, k = map(int, input().split())
    arr = [int(_) for _ in input().split()]

    subs = []
    for i in range(k):
        if i < len(arr):
            inc = [0]
            mx_it, ind, it = 0, 0, 0
            mn = arr[0]
            for j in range(1, len(arr)):
                if arr[j] > arr[j-1] or arr[j] > mn:
                    it += 1
                    inc.append(it)
                    if it > mx_it:
                        mx_it = it
                        ind = j
                else:
                    it = 0
                    inc.append(it)
                    mn = arr[j]

            subs.append(arr[ind-inc[ind]:ind+1])
            del arr[ind-inc[ind]:ind+1]
        else:
            subs.append([arr[0]])
            del arr[0]

    subs.sort(key=lambda x: x[0])
    for i in subs:
        print(*i, end=" ")

# 7 4
# 8 1 2 4 2 6 7
