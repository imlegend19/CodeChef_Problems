a = [2, 3, 4, 5, 6]
x = 2
for i in range(len(a)):
    a[i] ^= x

print(a)
print(sum(a))
