# 최대 100개의 key
# 최대 힙

def enq(n) :
    global last
    last += 1 # 마지막 정점 추가
    heap[last] = n # 마지막 정점에 저장

    c = last
    p = c//2

    # 조건 검사 : 부모 존재, 부모 > 자식
    while p>0 and heap[p] < heap[c] : # 자식이 더 크면
        heap[p], heap[c] = heap[c], heap[p] # 교체
        c = p # 옮긴 후, 부모가 다시 자식
        p = c//2 # 그 위 부모
    return

def deq() :
    global last

    tmp = heap[1] # 루트 임시 저장
    heap[1] = heap[last] # 마지막 정점의 값을 루트로 이동
    last -= 1 # 마지막 정점 삭제
    p = 1
    c = p * 2 # 왼쪽 자식 번호
    while c <= last : # 자식이 하나 이상 있으면
        if c+1 <= last and heap[c] < heap[c+1] : # 오른쪽 자식도 존재 + 오른쪽이 더 크면
            c += 1 # 비교 대상을 오른쪽 자식으로 변경
        if heap[c] > heap[p] : # 자식이 더 크면
            heap[c], heap[p] = heap[p], heap[c] # 교체
            p = c #
            c = p * 2
        else : break
    return tmp

heap = [0] * 101  # 1 ~ 100
last = 0  # 완전이진트리 마지막 정점 번호

enq(5)
print(heap[1])
enq(15)
print(heap[1])
enq(8)
print(heap[1])
enq(20)
print(heap[1])

while last > 0 : # 남아있으면
    print(deq())
