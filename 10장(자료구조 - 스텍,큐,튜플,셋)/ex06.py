
# 튜플 대입 연산에 대한 실습
# 튜플 패킹(packing) : 튜플에가사 값을 저장하는 과정
# 튜플 언패킹(unpacking) : 튜플에서 값을 추출해서 변수에 대입하는 과정

# 값을 교환할 떄 : 일반적인 방법
x = 10
y = 20
temp = x
x = y
y = temp
print("값 변경후(x,y) : ",x,y)
print("-----------------------------------------------------")
# 값을 교환할 때 : 튜플 이용하는 방법
(a,b) = 100,200
print("값변경전 : ",(a,b))
(c,d)=(b,a) # 튜플에서 값 변경에는 빈 컵이 필요없다.
print("값 변경 후 : ", (c,d))

# 인자 값들이 서로 맞게끔 줘야 된다. 그렇지 않으면 not enough values to unpack (expected 3, got 2) 오류 발생
# (x,y,z) = (10,20)

# 여러개의 변수를 한번에 할당하는 방법
person = ("신은혁", 14 ,"중학생")
(name, age, student_grade) = person
print("name : ", name, "age : ", age, "student_grade : ", student_grade)