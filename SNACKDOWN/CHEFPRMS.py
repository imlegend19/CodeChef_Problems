import math


def check_semi_prime(num):
    if int(math.sqrt(num)) != math.sqrt(num):
        cnt = 0

        for i in range(2, int(math.sqrt(num)) + 1):
            while num % i == 0:
                num /= i
                cnt += 1

            if cnt >= 2:
                break

        if num > 1:
            cnt += 1

        return cnt == 2
    else:
        return False


def semi_prime_sequence(n):
    arr = []
    for i in range(n):
        if int(math.sqrt(i)) != math.sqrt(i):
            if check_semi_prime(i):
                arr.append(i)
    # print(arr)
    return arr


t = int(input())
ans = []
for i in range(t):
    n = int(input())
    arr = semi_prime_sequence(n)
    flag = 0
    for j in range(len(arr)):
        if check_semi_prime(n - arr[j]):
            flag = 1
            ans.append("YES")
            break
    if flag == 0:
        ans.append("NO")

for e in ans:
    print(e)
