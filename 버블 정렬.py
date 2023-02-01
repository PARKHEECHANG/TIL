lst = list(map(int, input().split())) # input : 55 7 78 12 42
for i in range(len(lst)-1, 0, -1) : # 각 구간의 끝 (1씩 감소)
    for j in range(i) : # 비교할 왼쪽 원소
        if lst[j] > lst[j+1] :
           lst[j], lst[j+1] = lst[j+1], lst[j]

print(lst)
# [7, 12, 42, 55, 78]
