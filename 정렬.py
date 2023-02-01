# 버블 정렬
lst = list(map(int, input().split()))
for i in range(len(lst)-1, 0, -1) : # 각 구간의 끝 (1씩 감소)
    for j in range(i) : # 비교할 왼쪽 원소
        if lst[j] > lst[j+1] :
           lst[j], lst[j+1] = lst[j+1], lst[j] # 큰 원소 오른쪽으로

print(lst)


# 선택 정렬
lst = list(map(int, input().split()))

for i in range(len(lst)) :
    idx = i
    for j in range(i+1, len(lst)) :
        if lst[j] < lst[idx] :
            idx = j
    lst[idx], lst[i] = lst[i], lst[idx]

print(lst)


