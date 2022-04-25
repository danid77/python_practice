
# mutable object 중 dictionary라는 타입이 있다.
# 딕셔너리라는 타입의 형태는 키와 값의 쌍으로 이루어져 있다.
# 딕셔너리의 키의 값은 변경이 불가능하므로 유니크한 값이 되어야한다.
# 반대로 값은 변경이 가능하다.
# 딕셔너리의 call by reference가 성립되는 이유는 변경이 가능한 mutable object이기 때문에
# 가능한 것이다. call by objective-reference 라고도 칭한다.

def change(dic):
    print("change()내의 연산전 dic값 : ", dic)
    print("change()내의 연산전 dic의 주소(id) : ", id(dic))
    dic["weight"] = 85
    print("change()내의 연산후 dic값 : ", dic)
    print("change()내의 연산후 dic의 주소(id) : ", id(dic))


dic = {"name":"jin", "age":14, "height":180}
print(dic)

# 키를 주고 값을 얻어온다.
print(dic["name"])

print("--------------------------------------------")

print("호출 전 dic의 주소 값(id) : ", id(dic))
print("호출 전 dic의 값", dic)
change(dic)
print("--------------------------------------------")
print("호출 후 dic의 값", dic)
print("호출 후 dic의 주소 값(id) : ", id(dic))