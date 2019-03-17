def fibs(M, N, A, B):
    n = 0
    result = 0;
    fib = [0, 1, 2]
    n = max(2, N)
    while (len(fib) < n + 1):
        fib.append(0)
    fib[1] = A
    fib[2] = B

    for k in range(3, n + 1):
        fib[k] = fib[k - 1] + fib[k - 2]
    result = fib[n]
    ans1 = result % ((10 ** 9) + 7)
    print(ans1)


T = int(input())
while (T > 0):
    sumA = 0
    sumB = 0
    mandn = input().split()
    N = int(mandn[1])
    M = int(mandn[0])

    A = input().split()
    B = input().split()
    for j in range(0, M):
        sumA = sumA + (M * int(A[j]))
        sumB = sumB + (M * int(B[j]))
    # call func
    fibs(M, N, sumA, sumB)
    T = T - 1