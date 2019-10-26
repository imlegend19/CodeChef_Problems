import sys

if __name__ == '__main__':
    t = int(input())
    while t:
        n, k, p = map(int, input().split())
        arr = [int(_) for _ in input().split()]

        max_ind, min_ind = None, None

        if p == 0:
            mx = max(arr)
            if arr.count(mx) == 1:
                max_ind = arr.index(mx)
            else:
                if k % 2 == 0:
                    sm = -1
                    for i in range(n):
                        if i == 0:
                            if arr[i] == mx:
                                sm = arr[i + 1]
                                max_ind = i
                        elif i == n-1:
                            if arr[i] == mx and arr[i-1] > sm:
                                sm = arr[i-1]
                                max_ind = i
                        elif arr[i] == mx:
                            val = (arr[i-1] + arr[i+1])
                            if val > sm:
                                sm = val
                                max_ind = i
                else:
                    sm = sys.maxsize
                    for i in range(n):
                        if i == 0:
                            if arr[i] == mx:
                                sm = arr[i + 1]
                                max_ind = i
                        elif i == n - 1:
                            if arr[i] == mx and arr[i - 1] < sm:
                                sm = arr[i - 1]
                                max_ind = i
                        elif arr[i] == mx:
                            val = (arr[i - 1] + arr[i + 1])
                            if val < sm:
                                sm = val
                                max_ind = i
        else:
            mn = min(arr)
            if arr.count(mn) == 1:
                min_ind = arr.index(mn)
            else:
                sm = sys.maxsize
                for i in range(n):
                    if i == 0:
                        if arr[i] == mn:
                            sm = arr[i + 1]
                            min_ind = i
                    elif i == n-1:
                        if arr[i] == mn and arr[i-1] < sm:
                            sm = arr[i-1]
                            min_ind = i
                    elif arr[i] == mn:
                        val = (arr[i - 1] + arr[i + 1])
                        if val < sm:
                            sm = val
                            min_ind = i

        if p == 0:
            if k & 1:
                print(arr[max_ind])
            else:
                if max_ind == 0:
                    print(arr[max_ind+1])
                elif max_ind == n-1:
                    print(arr[max_ind-1])
                else:
                    if arr[max_ind-1] < arr[max_ind] and arr[max_ind-1] < arr[max_ind+1]:
                        print(arr[max_ind-1])
                    else:
                        print(arr[max_ind+1])
        else:
            if k & 1:
                print(arr[min_ind])
            else:
                if min_ind == 0:
                    print(arr[min_ind+1])
                elif min_ind == n-1:
                    print(arr[min_ind-1])
                else:
                    if arr[min_ind-1] > arr[min_ind] and arr[min_ind-1] > arr[min_ind+1]:
                        print(arr[min_ind-1])
                    else:
                        print(arr[min_ind+1])

        t -= 1
