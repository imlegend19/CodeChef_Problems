def fun():
    n = int(input())
    str1 = input()

    list1 = str1.split(" ")
    s = 0
    l1 = n - 1
    print(list1[l1][::-1], end=" ")
    l1 = l1 - 1
    for i1 in range(int(n) - 1):
        if i1 % 2 != 0:
            print(list1[l1], end=" ")
            l1 = l1 - 1
        else:
            print(list1[s], end=" ")
            s = s + 1
    print()


t = int(input())
for i in range(t):
    fun()
