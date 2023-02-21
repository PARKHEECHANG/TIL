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
    summ += arr[m+i] # 끝 인덱스 늘리기,  ~arr[n-1]
    if summ > maxx :
        maxx = summ

print(maxx)
```
