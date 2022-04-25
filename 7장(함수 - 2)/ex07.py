
# 지역변수와 전역변수의 실습

def test():
    # print(text) : UnboundLocalError: local variable 'text' referenced before assignment
    # 함수 안에서 하나의 변수가 전역변수가 되었다가 다시 지역변수가 될 수가 없다.
    text = "파이썬 공부"
    print(text)

text = "java study"
test()
print(text)

print("-------------------------------------------")

# 전역변수를 함수 안에서 값을 변경하고자 한다면...global 키워드를 사용하면 가능하다.
def test():
    # test() 함수 안에서 전역변수인 text를 사용하겠다는 것을 인터프리터에게 알린다.
    global text
    add = "text 지역변수 함수 내부 : "
    text = "파이썬 공부" # 전역변수의 값을 변경하고 있다.
    print(add + text)

text = "java study"
print("text 전역변수 변경전 : ", text)
test()
print("text 전역변수 변경후 : ",text)