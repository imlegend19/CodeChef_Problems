t = int(input())
dict = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6, 'g':7, 'h':8, 'i':9, 'j':10, 'k':11, 'l':12, 'm':13,'n':14, 'o':15,
        'p':16, 'q':17, 'r':18, 's':19, 't':20, 'u':21, 'v':22, 'w':23, 'x':24, 'y':25, 'z':26}
rand = ''
sum = 0
for i in range(t):
    x = map(int,input().split())
    y = map(str,input().split())

    n = x[0]
    k = x[1]
    s = str(y[0])
    cnt_letter = len(s)
    for q in s:
        rand.join(str(dict[q]))
    cnt_number = len(rand)
    for l in rand:
        sum = sum + int(l)
    power1 = cnt_letter - cnt_number + sum/k
    power2 = cnt_letter
    power3 = sum/k
    list_power = [power1,power2,power3]
    print(max(list_power),"1")

