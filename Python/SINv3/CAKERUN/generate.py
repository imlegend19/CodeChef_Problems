import random

foo = ['+', '.', '-']
for i in range(900):
    print(random.choices(population=foo, weights=[0.3, 0.2, 0.3])[0], end="")

# lst = []
# for i in range(200):
#     lst.append('.')
# for i in range(400):
#     lst.append('+')
#
# random.shuffle(lst)
#
# print("".join(lst))

# lst = []
# for i in range(100):
#     lst.append('+')
# for i in range(50):
#     lst.append('-')
# for i in range(47):
#     lst.append('.')
#
# random.shuffle(lst)
# print("".join(lst))
