```
# Two pointer
n, m = map(int, input().split()) # n개의 리스트, 합이 m이 되는 경우의 수

arr = list(map(int, input().split()))
cnt = summ = 0
ed = st = 0

while 1 :
    # m보다 크거나 같은 경우, 또는 이미 끝 인덱스 도달
    if summ >= m or ed == n :
        # 기존 시작 인덱스 값 빼주고
        summ -= arr[st]
        # 시작 인덱스 밀기
        st += 1

    # m보다 작은 경우
    elif summ < m :
        # 끝 인덱스 값 더하고
        summ += arr[ed]
        # 끝 인덱스 밀기
        ed += 1

    # 합에 정확히 도달하면
    if summ == m :
        # 카운트
        cnt+=1

    # 시작 인덱스가 끝까지 도달하면
    if st == n  : break

print(cnt)
```
