n = int(input())

for i in range(0, n):
    t = int(input())
    if t % 9 == 3 or t % 9 == 2:
        print('Sailaja')

    else:
        print('Supraja')