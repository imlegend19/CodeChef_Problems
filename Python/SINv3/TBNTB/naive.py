def next_power(n):
    count = 0

    if n and not (n & (n - 1)):
        return n

    while n != 0:
        n >>= 1
        count += 1

    return 1 << count


if __name__ == '__main__':
    t = int(input())
    while t:
        n = int(input())
        arr = [i for i in range(1, n+1)]

        xor = 0
        for i in range(n):
            arr[i] -= next_power(arr[i])
            xor ^= arr[i]

        if xor & 1:
            print("TO BE")
        else:
            print("NOT TO BE")

        t -= 1
