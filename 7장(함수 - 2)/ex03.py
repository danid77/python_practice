
# CALL by reference 에 대한 실습
# 함수를 호출할 때, 실질적인 주소값이 넘어가서 호출한 곳에 영향을 끼치는 형태가 된다.
# 파이썬에서는 함수의 매개변수값이 전부 객체인데 list, dictionary(딕셔너리)와 같은
# mutable object즉 변경가능한 객체이므로 call by objective-reference 라고한다.

def change(li):
    print("change()내의 연산전 li값 : ", li)
    print("change()내의 연산전 li의 주소(id) : ", id(li))
    li += [100,200]
    print("change()내의 연산후 li값 : ", li)
    print("change()내의 연산후 li의 주소(id) : ", id(li))

print("--------------------------------------------")

list = ["안녕", 1, 3, 1, 1.1]
print("호출 전 list의 주소 값(id) : ", id(list))
print("호출 전 list의 값", list)
change(list)
print("--------------------------------------------")
print("호출 후 list의 값", list)
print("호출 후 list의 주소 값(id) : ", id(list))
    