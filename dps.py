def check_palindrome(s):
    return s == s[::-1]


if __name__ == '__main__':
    t = int(input())
    while t != 0:
        s = input()
        x = set()
        for i in s:
            x.add(i)
        n = len(s) + 1
        if len(x) > n/2 + 1:
            print("!DPS")
        else:
            check = check_palindrome(s)
            if check and len(s) % 2 == 0:
                print("!DPS")
            else:
                print("DPS")

        t -= 1
