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

```
# return 차이
sum += edge[cur][i] 
dfs(i, sum)

dfs(i, sum+edge[cur][i])
```

```
# Sliding Window
n, m = map(int, input().split()) # n개의 리스트, 연속된 m개의 합

arr = list(map(int,input().split()))

summ = 0
# 첫 m개 구간의 합
for i in range(m) :
    summ += arr[i]

maxx = summ

for i in range(n-m) :
    summ -= arr[i] # 첫 인덱스 줄이기
    summ += arr[m+i] # 끝 인덱스 늘리기
    if summ > maxx :
        maxx = summ

print(maxx)
```
