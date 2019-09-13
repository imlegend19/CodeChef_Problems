import math
ans = []
t = int(input())
for i in range(t):
    n = int(input())
    bit_count = 0
    nibble_count = 0
    byte_count = 0
    x = math.floor(n/16)
    bit_count += x*2
    y = math.floor((n-x)/8)
    byte_count += y
    z = math.floor((n-x-y)/2)
    nibble_count += z
    bit_count += (n-x-y-z)

    s = ""
    s += str(bit_count) + " " + str(nibble_count) + " " + str(byte_count)
    ans.append(s)

for e in ans:
    print(e)
