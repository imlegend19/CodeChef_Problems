# database of clients

# 2
# 1.2.3@testing
# testing@1.2.3

# 7
# alice@e.mail
# eve@another.mail
# bob@e.mail
# joe90@e.mail
# b.o.b@e.mail
# bob+new@e.mail
# bob@another.provider


def remove_occ(string):
    return string.replace('.', '')


if __name__ == '__main__':
    n = int(input())
    providers = {}
    for i in range(n):
        s = input().split('@')
        try:
            providers[s[1]].add(remove_occ(s[0].split('+')[0]))
        except Exception:
            providers[s[1]] = {remove_occ(s[0].split('+')[0])}

    cnt = 0
    for i in providers.values():
        cnt += len(i)

    print(cnt)
