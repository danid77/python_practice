import math
from math import *
# 원의 면적과 원의 둘레를 구하는 프로그램을 작성
# PI = 3.141592 전역상수를 선언하고 상수를 활용하도록 한다.

pi = math.pi

# 면적을 구하는 함수
def mun(r):
    result = pi*(r**2)
    return result

# 둘래를 구하는 함수
def due(r):
    result = 2*pi*r
    return result

# 프로그램을 시작하는 함수
def main():
    r = int(input("정수를 입력하세요"))
    result1 = mun(r)
    result2 = due(r)

    print("면적 : ", round(result1,2))
    print("둘래 : ", round(result2,2))

main()