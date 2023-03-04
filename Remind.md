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
```
---
int(a/b)와 a//b는 모두 두 정수 a와 b의 나눗셈 결과를 정수로 변환하는 것을 의미하지만, 두 연산에는 약간의 차이가 있습니다.

int(a/b)는 먼저 a/b를 계산하고, 이 값을 정수로 변환합니다. 이 때, 정수로 변환되기 전에는 실수값이라면 소수점 이하를 버립니다. 예를 들어, int(7/2)의 결과는 3이 됩니다.

반면, a//b는 Python에서 정수 나눗셈 연산자입니다. 이 연산자는 a/b를 계산하고, 이 값을 소수점 이하를 버리고 나머지를 버리고 가장 가까운 정수로 변환합니다. 예를 들어, 7//2의 결과는 3이 됩니다.

따라서, int(a/b)와 a//b의 결과는 a/b의 값이 정확하게 정수일 때는 같지만, a/b가 실수일 때는 다를 수 있습니다. 또한, a/b의 값이 음수인 경우 int(a/b)는 소수점 이하를 버리므로 다른 결과가 나올 수 있습니다. 예를 들어, -7//2의 결과는 -4가 되지만, int(-7/2)의 결과는 -3이 됩니다.
