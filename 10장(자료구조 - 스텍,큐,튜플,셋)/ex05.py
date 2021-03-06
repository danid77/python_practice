
# 튜플에 대한 실습
# 튜플의 특징 : 리스트에 반해서 변경이 불가능한 객체 이다. 리스트에 비해서 속도가 빠르다.
# 시퀀스의 일종이다
# +, * min(), len(),cmp(), tuple() 연산과 내장함수가 사용이 가능하다.
# 리스트는 대괄호[], 튜플은 소괄호()로 요소를 감싼다.

colors = ("red", "blue", "yellow")
print(colors)
print(type(colors))

# 튜플도 리스트와 마찬가지로 여러가지 자료형을 섞어서 생성할 수 있다.
tuple1 = (1, 2.2, "하이")
print(tuple1)

# 공백 튜플 만들기
tuple2 = ()
# 튜플은 한번 생성되면 더이상 추가, 삭제, 수정이 불가능한다.
# tuple2[0] = 100 : 의미 없는 코드

# 하나의 값만을 가지는 튜플을 생성 할때는 반드시 요소 뒤에 ,(콤마)를 적어야 한다.
# 그렇지 않으면 일반 정수나 문자열로 인식한다.
tuple3 = (10,)
print(tuple3)
print(type(tuple3))

li = [1,2,3,4,5]
# 리스트를 내장함수인 tuple()로 tuple로 만들수가 있다.
tuple4 = tuple(li)
print(li)
print(tuple4)

# 튜플도 리스트와 마찬가지로 내장 튜플을 가질 수 있다.
t1 = (1,2.2,"반가워요")
t2 = t1, (3.3,4.4,5.5)
print("t1의 주소 : ", id(t1))
print("t2의 주소 : ", id(t2))
print("t2[0]의 주소 : ", id(t2[0]))
print("t2[1]의 주소 : ", id(t2[1]))

print("\n")

t1 = (1,2.2,"반가워요")
t2 = (3.3,4.4,5.5)
t3 = t1, t2
print("t1의 주소 : ", id(t1))
print("t2의 주소 : ", id(t2))
print("t3의 주소 : ", id(t3))
print("t3[0]의 주소 : ", id(t3[0]))
print("t3[1]의 주소 : ", id(t3[1]))

# 서로 다른 데이터 타입의 튜플의 요소로 존재한다면 비교가 되질 않는다.
t4 = (1,2.2,3,"안녕")
t5 = (1,2,2,3)
print("t4의 길이 : ", len(t4))
# print("t4의 가장 큰 값 : ", max(t4)) not supported between instances of 'str' and 'int'에러
print("t5의 가장 큰 값 : ", max(t5))
print("t5의 가장 작은 값 : ", min(t5))

t6 = (1,2.2,3,"안녕")
t7 = (1,2.2,3)
t8 = t6 + t7    # 튜플은 + 연산이 가능하다(접합)
print(t8)
t9 = t7 * 2     # 튜플은 * 연산도 가능하다(반복)
print(t9)

if 2.2 in t6:       # 존재 여부를 알아봄
    print("t6에는 2.2가 존재합니다.")
# 튜플은 시퀀스의 일종이니 반복문도 가능하다.
for x in range(len(t6)):
    print(x,end=" ")
print()
print("-----------------------------------------------------")

# 인덱싱
t10 = (1, 2.2, 3,"안녕", "철수", 5.5)
print(t10[4])
print(t10[-1])
print(t10[1:])
# 슬라이싱
print(t10[4:6])
print(t10[-3:-1])   # 앞에 있는것부터 슬라이싱해서 들어감

# dir() 함수는 사용할 수 있는 함수들을 출력해주는 역할을 하는 함수이다.
t1 = (1,2.2,3)
t2 = (1,2.2,3)
print(dir(t1))
# 튜플을 비교를 하자고 한다면 __eq__()을 사용한다.
print(t1.__eq__(t2))
