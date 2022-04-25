import math
from math import *
# 문제 : 원의 넓이와 둘래를 동시에 반환하는 함수를 작성하고 테스트 하라.
# 반지름은 사용자로부터 입력을 받는다.
# 출력 결과
# 원의 반지름을 입력하시오: 10
# 원의 넓이는 314.1592653589793이고 원의 둘레는 62.83185307179586이다.
# 반지름 : raidus ,넓이 : area, 둘래 : circim














print("========================================")
print("선생님 풀이")



def calcCircle(raidus):
    # 넓이
    area = math.pi * raidus * raidus
    # 둘래
    circim = 2 * math.pi * raidus
    # 값을 다중으로 넘기고 싶을 때 튜플을 사용하면 된다.
    return (area, circim)

if __name__ == "__main__":
    radius = float(input("원의 반지름을 입력하세요."))
    (area, circim) = calcCircle(radius)
    print("원의 넓이는",area,"이고 원의 둘레는 ",circim,"이다.")