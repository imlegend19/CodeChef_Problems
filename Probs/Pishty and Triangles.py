n,q = map(int,raw_input().split())   # n = 5     q = 2
x = map(int,raw_input().split())    # x = [1,2,3,4,5]
lst = list()      # lst = [[2,2,4],[1,2,5]]
ans = []        # ans = [0]
def isPossibleTriangle(arr, N):
    if N < 3:
        return False
    arr = x[l-1:r]
    arr.sort(reverse=True)
    count = 0
    i = 0
    while (i<N-2):
        if (arr[i] < arr[i + 1] + arr[i + 2]):
            if count<(arr[i]+arr[i+1]+arr[i+2]):
                count = 0
                count += arr[i]+arr[i+1]+arr[i+2]
        i+=1
    return count
for _ in range(q):
    x1 = map(int,raw_input().split())
    lst.append(x1)
for i in range(len(lst)):
    pos_val = lst[i][0]
    l = lst[i][1]
    r = lst[i][2]
    if pos_val == 2:
        ans.append(isPossibleTriangle(x,r-l+1))
    elif pos_val == 1:
        x[l-1] = r
    else:
        break

for ele in ans:
    print ele


