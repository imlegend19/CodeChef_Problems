from collections import defaultdict


def get_anagrams(words):
    grouped_words = defaultdict(list)

    for word in words:
        grouped_words["".join(sorted(word))].append(word)

    return len(grouped_words.values())


if __name__ == "__main__":
    n = int(input())
    wrd = []
    for i in range(n):
        wrd.append(input())

    q = int(input())
    for _ in range(q):
        l, r = map(int, input().split())
        print(get_anagrams(wrd[l-1:r]))
