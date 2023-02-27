lst = 'ABCD'
n = int(input())
path = [0] * n

def abc(lv, st):

    for i in range(lv) :
        print(path[i], end='')
    print()

    if lv == n :
        return

    for i in range(st, 4):
        path[lv] = lst[i]
        abc(lv+1, i+1)

abc(0, 0)
