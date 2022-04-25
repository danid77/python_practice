
# 지역변수와 전역변수에 대한 실습
# 지역변수 : 함수 내에 정의된 변수, 범위는 함수 내에서만 사용되고 함수가 호출되고 종료되면 지역변수는 소멸된다.
def test():
    text = "파이썬 공부"     # 지역변수 text에 문자열 할당
    print(text)            # 출력함수를 이용하여 text를 출력함

# test()를 호출한 후, "파이썬 공부"라는 문자열을 출력하면서 리턴 값은 없다.
test()
# print(text) : NameError: name 'text' is not defined
# text 변수가 정의도지 않았기 떄문에 오류 발생
# test()의 text라는 변수는 지녁변수이므로 함수 호출 후 소멸된다. 
