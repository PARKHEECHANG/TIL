``` python
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
```

``` python
# 두 팀으로 나눠 전투력 차이의 최솟값 측정

player = [49, 6, 54, 80, 3, 18, 71]
visit = [0] * 7
path = [0] * 7
Min = 21e8

# 부분집합
def dfs(lv, st) :
    global Min

    for i in range(lv):
        print(path[i], end=' ')
    print()

    if lv == 6 :
        return

    team_1 = team_2 = 0

    for i in range(7) :
        if visit[i] == 0 :
            team_1 += player[i]
        elif visit[i] == 1 :
            team_2 += player[i]

    if abs(team_1 - team_2) < Min :
        Min = abs(team_1 - team_2)

    for i in range(st, 7) :
        if visit[i] == 0 :
            path[lv] = player[i]
            visit[i] = 1
            dfs(lv+1, i+1)
            visit[i] = 0

dfs(0, 0)
print('ans', Min)
```
