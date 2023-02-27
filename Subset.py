lst = 'ABCD'
n = int(input())

path = [0] * n

def dfs(lv, st) :

    for i in range(lv) :
        print(path[i], end='')
    print()

    if lv == n :
        return

    for i in range(st, 4) :
        path[lv] = lst[i]
        dfs(lv+1, i+1)

dfs(0, 0)
