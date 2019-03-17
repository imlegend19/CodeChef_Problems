t =  int(input())
ans = []
for _ in range(t):
    str = raw_input()
    vowel_count = 0
    cons_count = 0
    vowels = frozenset('aeiou')
    cons = frozenset('bcdfghjklmnpqrstvwxyz')
    vowel_count += sum(1 for c in str if c in vowels)
    cons_count += sum(1 for c in str if c in cons)
    ans.append([vowel_count,cons_count])
for j in range(len(ans)):
    print '{0}  {1}'.format(ans[j][0],ans[j][1])
