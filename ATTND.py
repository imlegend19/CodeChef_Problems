if __name__ == '__main__':
    t = int(input())

    while t != 0:
        n = int(input())

        arr = []
        dic = {}
        for i in range(n):
            temp = input()
            arr.append(temp)
            first = temp.partition(' ')[0]
            if first in dic:
                dic[first] += 1
            else:
                dic[first] = 1

        for i in arr:
            temp = i.partition(' ')[0]
            if dic.get(temp) > 1:
                print(i)
            else:
                print(temp)

        t -= 1
