if __name__ == '__main__':
    t = int(input())
    vowels = ['a', 'e', 'i', 'o', 'u']
    while t != 0:
        n = int(input())
        s = input()
        count = 0
        prev_consonant = False
        for i in range(n):
            if s[i] in vowels:
                if prev_consonant:
                    count += 1
                prev_consonant = False
            else:
                prev_consonant = True

        print(count)

        t -= 1
