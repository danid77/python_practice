
# 문자열 전달에 대한 실습
# 문자열에 대한 내용도 앞서 살펴본 숫자형의 객체와 동일한 변경이 될 수 없는 immutable object 형태이다.
# 파이썬의 경우는 타 언어의 call by value의 개념과는 조금은 다르다.
# 그 이유는 파이썬은 모든 것을 "객체"로 판단을 하기 떄문인 것이다.
# 파이썬의 이런 특성이 존재하므로 call by objective 이라고도 칭한다.

def change(string):
    print("change()내의 연산전 string값 : ", string)
    print("change()내의 연산전 n의 주소(id) : ", id(string))
    string+=" 공부합니다."
    print("change()내의 연산후 string값 : ", string)
    print("change()내의 연산후 n의 주소(id) : ", id(string))    # 새로운 객체 생성

msg = "안녕하세요 저는 파이썬을"
print("호출 전 msg의 주소 값(id) : ", id(msg))
print("호출 전 msg의 값", msg)
change(msg)
print("호출 후 msg의 값", msg)
print("호출 후 msg의 주소 값(id) : ", id(msg))