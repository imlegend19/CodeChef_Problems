MOD = 10 ** 9 + 7


def is_lucky(n1, lst: list):
    if lst.count(n1) > 1:
        return True
    else:
        return False


def get_inv(n1):
    return pow(n1, MOD - 2, MOD)


def c(n1, k1):
    if n1 < k1 or k1 < 0:
        return 0
    global fact, rfact
    return (fact[n1] * rfact[k1] * rfact[n1 - k1]) % MOD


fact = [1]
rfact = [1]

for i in range(1, 100500):
    fact.append((i * fact[-1]) % MOD)
    rfact.append((get_inv(i) * rfact[-1]) % MOD)

n, k = map(int, input().split())
a = list(map(int, input().split()))

d = dict()
for x in a:
    if is_lucky(x, a):
        d[x] = d.get(x, 0) + 1

dp = [0 for i in range(len(d) + 2)]

dp[0] = 1
for x in d:
    for i in range(len(dp) - 1, 0, -1):
        dp[i] += dp[i - 1] * d[x]
        dp[i] %= MOD

unlucky = n - sum(d.values())
ret = 0

for K in range(k+1):
    for i in range(len(dp)):
        if K >= i:
            ret += dp[i] * c(unlucky, K - i)

print(ret % MOD)
