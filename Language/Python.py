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

n = input()
if(n.isupper()) :           # if(65 <= ord(n) <= 90) :
    print("대문자입니다")    #     print("대문자입니다")
elif (n.islower()) :        # elif(97 <= ord(n) <= 122) :
    print("소문자입니다")    #     print("소문자입니다")


# 전역 변수 global
# 함수 외부에서 선언된 변수, 함수 내에서 global 키워드로 재선언해야 접근 가능

n = 0
print(id(n)) # 주소값
# 출력 : 2424264026384

print("""줄
바
꿈""")

bool(0) = False
bool(1) = True
bool(123123) = True
bool(-1) = True


lst = [1,2,3,4,5]
print(*lst) # 괄호, 콤마 제거 후 출력
1 2 3 4 5

# set - 리스트 중복 제거
lst = [2,2,2,2,2,3,3,3,1,1,1,5,5,4]
lst = set(lst)
print(lst)
