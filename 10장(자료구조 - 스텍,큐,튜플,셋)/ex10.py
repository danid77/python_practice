# 부분 집합 연산

SET1 = {10,20,30}
SET2 = {10,20,30}
# 2개의 세트가 같은지를 검사하는 방법(==, !=)
print("SET1과 SET2가 같은가? :", SET1 == SET2)
print("SET1과 SET2가 다른가? :", SET1 != SET2)
print("------------------------------")

# 부등호 연산을 이용하여 부분집합인지 아닌지를 알수 있는 방법
# 진상위 집합의 개념 : SET2집합이 SET1집합에 포함되지만 서로 집합은 동일하지
# 않은 집합을 의미한다. SET2집합은 SET1집합과 동일하지 않다.(길이가 다름)
SET1 = {10,20,30,40,50,60}
SET2 = {10,20,30}
# 연산자를 이용한 방법
print("SET2는 SET1에 부분집합인가? :", SET1 > SET2)
# issubset() 을 이용한 방법
print("SET2는 SET1에 부분집합인가? :", SET2.issubset(SET1))
print("------------------------------")

# 상위 집합인지 확인하는 방법
# 부등호로써는 확인할 수 있는 방법은 없다.
# print("SET1은 SET2에 상위집합인가? :", SET1 >= SET2)
# issuperset() 를 이용하는 방법
print("SET1은 SET2에 상위집합인가? :", SET1.issuperset(SET2))
print("------------------------------")

# 데이터값이 집합에 포함되어있는지 확인하는 방법
SET_STRING = set("안녕하세요.")
print(SET_STRING)   # 하나하나 나눠져서 추가됨
if "안" in SET_STRING:
    print("'안' 문자는 SET_STRING 세트에 포함되어 있습니다.")

print("------------------------------")
# 집합연산을 할 수 있는 것이 세트라는 자료구조의 장점이다.
# 합집합 : 연산자 |(파이프, or), union() 메서드를 사용
SET1 = {10,20,30,40,50,60}
SET2 = {10,20,30}
print("|연산자 합집합 :", SET1 | SET2)
print("union() 합집합 :", SET1.union(SET2))
print("union() 합집합 :", SET2.union(SET1))

print("------------------------------")

# 교집합은 두 개의 집합에서 겹치는(공통적인) 요소를 구하는 연산이다.
# 방법 : 연산은 &(and)를 사용하거나 intersection() 이용한다.
SET1 = {10,20,30,40,50,60}
SET2 = {10,20,30}
print("&연산자 교집합 :", SET1 & SET2)
print("intersection() 교집합 :", SET1.intersection(SET2))
print("intersection() 교집합 :", SET2.intersection(SET1))

print("------------------------------")

# 차집합은 하나의 집합에서 다른 집합의 요소를 빼고 남은 집합
# 방법 : 연산자 - 를 사용하거나, difference() 를 사용한다.
SET1 = {10,20,30,40,50,60}
SET2 = {10,20,30}
print("-연산자 차집합 :", SET1 - SET2)
print("difference() 차집합 :", SET1.difference(SET2))
# 차집합을 하고 난 뒤는 아무런 값이 없다.
print("difference() 차집합 :", SET2.difference(SET1)) # set() - 빈값으로 출력

print("------------------------------")

# all() : 집합에서 모든 값이 참이어야지만 참을 리턴해준다.
# any() : 집합에서 값이 하나라도 참이면 참을 리턴해준다.
# SET1 = {0,20,30,40,50,60}     False : 0때문에
SET1 = {10,20,30,40,50,60}
SET2 = {10,0,0,0,0,-7}
print("all()결과 : ", all(SET1))
print("any()결과 : ", any(SET2))

print("------------------------------")

# 집합이 첨부터 아에 다른지를 확인하고 싶을때(같은 요소가 없다)
SET1 = {10,20,30,40,50,60}
SET2 = {0,0,0,0,0,-7}
SET3 = {10,0,0,0,0,-7}
print("set1에서 set2와 같은 요소가 없는가 : ", SET1.isdisjoint(SET2))
print("set1에서 set3와 같은 요소가 없는가 : ", SET1.isdisjoint(SET3))

print("------------------------------")

# pop() 로 집합의 요소를 제거할 수 있는데, 임의로 아무요소나 삭제한다.
# 단, 정수의 경우는 한번 가져올때의 패턴을 재실행해도 똑같지만, 문자열 타입은
# 삭제 및 출력 패턴이 실행할 때마다 달라진다는 것을 알 수가 있다.
SET1 = {10,20,30,40,50,60}
print(SET1.pop())
print(SET1)

for _ in range(len(SET1)):
    print(SET1.pop(), end=" ")
print()
print("현재 SET1의 크기 : ", len(SET1))

SET1 = {"가나","한국","일본","미국","영국"}
print(SET1.pop())
print(SET1)

for _ in range(0, len(SET1)):   # 모든 요소 삭제
    print(SET1.pop(), end=" ")
print()
print("현재 SET1의 크기 : ", len(SET1))