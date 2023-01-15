N, K = map(int, input().split()) # 여러 정수 입력 받기

data = list(map(int, input().split())) # 여러 정수 리스트에 넣기

data.sort() # 정렬

data.sort(Reverse=True) # 내림차순 정렬
(int 변환 안하면 사전순으로 정렬되니 주의)

data = [input() for i in range(n)] #여러 줄 입력받기

data = list(input()) # 문자열의 문자 하나씩 리스트에 알아서 입력된다.

rows = 3
cols = 3
arr = [[0 for j in range(cols)] for i in range(rows)] # 이차원 리스트 선언(3x3)

for i in range(len(arr)) :
    for j in range(len(arr[i])) : # 이차원 리스트 반복문
    
list = [0 for i in range(n)] # 리스트 길이 지정

              ####리스트 병합, 추가####
        l = list(map(int, input().split()))
        n = int(input())
        l2 = [n,n+1,n+2]
        l += l2

        l = list(map(int, input().split()))
        n = int(input())
        l += [n,n+1,n+2]

        l = list(map(int, input().split()))
        n = int(input())
        for i in range(3) :
            l += [n]                # 리스트 요소 추가할 때 대괄호
            n+=1
        ##########################################

ord('A') # A를 아스키코드로 변환
chr(65) # 아스키코드를 문자로 변환
