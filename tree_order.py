'''
13
1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13
'''

def preoredr(i) :
    if i : # 존재하는 정점이면
        print(i, end = ' ')
        preoredr(left[i])
        preoredr(right[i])
    return

def inoredr(i) :
    if i : # 존재하는 정점이면
        inoredr(left[i])
        print(i, end = ' ')
        inoredr(right[i])
    return

def postoredr(i) :
    if i : # 존재하는 정점이면
        postoredr(left[i])
        postoredr(right[i])
        print(i, end = ' ')
    return


V = int(input())
arr = list(map(int, input().split()))
E = V - 1 # 간선 수
left = [0] * (V+1) # 부모를 인덱스로 왼쪽 자식 저장
right = [0] * (V+1) # 부모를 인덱스로 오른쪽 자식 저장
par = [0] * (V+1)
# child = [ [] for _ in range(V+1) ]
for i in range(E) :
    p, c = arr[i*2], arr[i*2+1]
    if left[p] == 0 :
        left[p] = c
    else :
        right[p] = c
    par[c] = p

root = 1
while par[root] != 0 :
    root += 1
preoredr(3)
print()
inoredr(3)
print()
postoredr(3)
