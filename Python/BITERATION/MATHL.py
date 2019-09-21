all_ns = []
dic = {}

if __name__ == '__main__':
    t = int(input())
    while t != 0:
        n = int(input())
        prod = 1

        for i in range(1, n+1):
            prod *= i**(n-i+1) % 1000000007

        print(prod % 1000000007)

        t -= 1
