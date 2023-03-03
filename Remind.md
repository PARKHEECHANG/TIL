* 중복되지 않는 순위는 인덱스와 그 값 즉, 하나의 배열로 활용 가능
* 두 값에서 한 쪽을 정렬했다면 다른 한 쪽 값만 고려해볼 것
* 문제를 풀기 전, 복잡도 계산+타입 설정 주의 int,long,double]

```python
# 2차원 리스트 주소값 차이
lst = [ [0] * 4 ] * 4
lst2= [ [0 for i in range(4)] for i in range(4) ]

print(lst)
print(lst2)

lst[0][0] = 1
lst2[0][0] = 1

print(lst)
print(lst2)
```

```python
# return 차이
sum += edge[cur][i] 
dfs(i, sum)

dfs(i, sum+edge[cur][i])
```

``` python
# [1] 섬 개수
# [2] 가장 큰 섬 size
# [3] 가장 작은 섬 size

# bfs 호출 마다 섬 개수 ++
# bfs 호출 결과를 MAX, MIN

def bfs() :
    size = 0

    while q :
        y, x = q.pop(0)
        size += 1

        for dy, dx in ((0,-1),(0,1),(-1,0),(1,0)) :
            ny, nx = dy + y , dx + x

            if ny < 0 or nx < 0 or ny > 4 or nx > 4 : continue
            if arr[ny][nx] == 0 : continue
            arr[ny][nx] = 0
            q.append((ny,nx))

    return size

arr = [[0,0,1,0,1],
       [0,0,1,0,1],
       [0,1,1,1,0],
       [0,0,1,0,0],
       [1,0,0,1,1]]

q = []
land_cnt = 0
MAX_size = 0
MIN_size = 21e8
for i in range(5) :
    for j in range(5) :
        if arr[i][j] == 1 :
            q.append((i, j))
            arr[i][j] = 0
            size = bfs()
            MAX_size = max(MAX_size, size)
            MIN_size = min(MIN_size, size)
            land_cnt += 1

print(land_cnt)
print(MAX_size)
print(MIN_size)
```python
