if __name__ == '__main__':
    t = int(input())
    while t != 0:
        inp = [int(_) for _ in input().split()]
        age = inp[:3]
        units = inp[3:]

        units = [x for _, x in sorted(zip(age, units), reverse=True)]
        age.sort(reverse=True)

        temp = inp[3:]
        temp.sort(reverse=True)

        print(temp)
        print(units)
        print(age)

        if temp == units:
            print("FAIR")
        else:
            print("NOT FAIR")

        t -= 1
