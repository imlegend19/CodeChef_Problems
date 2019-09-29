def count_frequency(my_list):
    freq = {}
    for item in my_list:
        if item in freq:
            freq[item] += 1
        else:
            freq[item] = 1

    return sorted(freq.values(), reverse=True)


if __name__ == '__main__':
    t = int(input())
    while t != 0:
        n, q = map(int, input().split())
        sz = [int(_) for _ in input().split()]

        count = count_frequency(sz)

        for i in range(q):
            k = int(input())

            print(sum(count[:k]))

        t -= 1
