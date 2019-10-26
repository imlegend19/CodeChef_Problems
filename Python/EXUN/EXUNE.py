import math

if __name__ == '__main__':
    t = int(input())
    while t != 0:
        n, k, m = map(int, input().split())
        if n == 1:
            num = ((pow(k+1, m) % 1000000007 + pow(k-1, m) % 1000000007) // 2) % 1000000007
            print(num)
        else:
            sm = math.factorial(k) % 1000000007
            for i in range(n):
                sm *= math.factorial(i+1) % 1000000007

            ans = (math.factorial(m) // 2*sm) % 1000000007

            print(ans)

        t -= 1
