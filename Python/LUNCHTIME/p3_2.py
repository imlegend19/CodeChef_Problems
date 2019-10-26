import sys

if __name__ == '__main__':
    t = int(input())
    while t:
        n, k, p = map(int, input().split())
        arr = [int(_) for _ in input().split()]

        if k % 2 != 0:
            if p == 0:
                print(max(arr))
            else:
                print(min(arr))
        else:
            if p == 0:
                mx = max(arr)
                mx_2 = -1
                for i in range(n):
                    if i == 0:
                        if arr[i] == mx:
                            mx_2 = arr[i + 1]
                    elif i == n-1:
                        if arr[i] == mx:
                            if arr[i - 1] > mx_2:
                                mx_2 = arr[i - 1]
                    else:
                        if arr[i] == mx:
                            val = min(arr[i + 1], arr[i - 1])
                            if val > mx_2:
                                mx_2 = val

                print(mx_2)
            else:
                mn = min(arr)
                mn_2 = sys.maxsize
                for i in range(n):
                    if i == 0:
                        if arr[i] == mn:
                            mn_2 = arr[i + 1]
                    elif i == n-1:
                        if arr[i] == mn:
                            if arr[i - 1] < mn_2:
                                mn_2 = arr[i - 1]
                    else:
                        if arr[i] == mn:
                            val = max(arr[i + 1], arr[i - 1])
                            if val < mn_2:
                                mn_2 = val

                print(mn_2)

        t -= 1
