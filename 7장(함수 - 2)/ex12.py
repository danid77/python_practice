
# 무명함수(익명함수, anonymous function)에 대한 실습
# 무명함수는 함수명이 없고, 구현부만 존재한다. 파이썬에서는 무명함수를 만들때 lambda 키워드로 만들수 있다.
# 무명함수는 print()등과 같은 일반함수를 호출할 수가 없다.
# 오직 계산만 가능하다.
# 전역변수를 참조 할 수 없다.
# lambda 인수1, 인수2 : 수식 <--- 문법

# 실행 함수
def main():
    print("두 정수의 합 : ", get_sum(10,50))
    print("두 정수의 합 : ", get_sum(100,50))
    print("람다식을 이용한 무명함수명 호출 결과 : ", sum(100,50))
    # 함다함수를 출력을 하면 결과론적으로 함수 객체를 출력하는 형태가 된다.
    print(lambda x, y: x + y)
    
    # 아래 코드가 실질적으로 람다식을 이용한 무명함수를 직접 호출한 형태
    print((lambda x, y: x + y)(10,50))

    for f in li:
        print(f(10))

# 일반적인 함수
def get_sum(x,y):
    return x + y

# lambda 키워드를 이용한 sum()만들기
# 람다함수는 코드 안에 함수를 포함하는 어느 곳이든지 다 사용가능하다.
# 가장 많이 사용되는 곳은 GUI프로그램에서 이벤트를 처리하는 콜백함수 형태로 많이 사용된다.
sum = lambda x,y:x+y

# 람다함수에서는 변수에 값을 할당할 수 없다.
# lambda x = 10, y : x+y

li = [lambda x : x**2, lambda x:x**3, lambda x:x**4]


main()