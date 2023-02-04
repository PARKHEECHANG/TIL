* 중복되지 않는 순위는 인덱스와 그 값 즉, 하나의 배열로 활용 가능
* (그리디) 두 값에서 한 쪽을 정렬했다면 다른 한 쪽 값만 고려해볼 것
* 배열이나 스택 등을 테스트케이스 반복문 밖에서 초기화하는 실수 조심

* 문제를 풀기 전, 복잡도 계산+타입 설정 주의 int,long,double]
* 메서드 선언, 스태틱 변수와 배열 활용

* 아스키 코드 48:'0', 65:'A', 97:'a'

* 변수명 짓기 https://www.curioustore.com/#!/

* 논리적 사고 == 작은 문제로 쪼개기

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
