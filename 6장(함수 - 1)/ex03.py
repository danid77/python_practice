
# 두개의 정수를 입력받아서 두 중 중에서 더 큰수를 찾아서 큰수를 리턴하는 함수
# 함수의 목록이 정의되어 있는 모듈을 import 할때는 항상 개발코드의 상위에 위차해야 한다.
# : 한줄 한줄 코드를 읽는 인터프리트 언어의 특성상 모듈코드를 하위에 작성하면 상위에 함수를
# 호출하는 코드는 에러가 발생한다.
def maxium(x, y):
    # return문은 최소화하는게 좋은 코드이다.
    temp = 0
    if x > y:
        temp = x
    else:
        temp = y
    return temp

num1 = int(input("첫번째 정수 : "))
num2 = int(input("두번째 정수 : "))
value = maxium(num1, num2)
print("최대값은 : ", value)

print("----------------------")

# 두개의 정수를 입력받아서 두 중 중에서 더 잗은 수를 찾아서 큰수를 리턴하는 함수
def minium(x, y):
    # return문은 최소화하는게 좋은 코드이다.
    temp = 0
    if x > y:
        temp = y
    else:
        temp = x
    return temp

num1 = int(input("첫번째 정수 : "))
num2 = int(input("두번째 정수 : "))
value = minium(num1, num2)
print("최대값은 : ", value)

print("----------------------")

# 두 수를 입력 받아서 거듭제곱을 구한다.
def power(x,y):
    result = 1
    for i in range(y):
        result *= x
    return result

num1 = int(input("첫번째 정수 : "))
num2 = int(input("두번째 정수 : "))

print(num1,"의",num2,"제곱값은 : ", power(2, 4))