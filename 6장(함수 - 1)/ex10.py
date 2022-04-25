
# 구의 부피를 계산하는 함수 sphereVolume()를 작성하시오
# 그리고, 반지름을 사용자로부터 입력받고 구의 부피를 구하는 함수를 호출해서 테스트 하라.
# 구의 부피 공식 : 4/3 * pi * r의 세제곱
import math
from math import *

def sphereVolume(radius):
    volume = (4.0/3.0)* math.pi * math.pow(radius, 3)
    return volume

radius = float(input("구의 반지름을 입력하시오 : "))
print("반지름이 ", radius, "인 구의 부피 : ", round(sphereVolume(radius),2))