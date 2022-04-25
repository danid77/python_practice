
# 주사위 눈을 랜덤으로 발생시켜 해당하는 숫자를 출력하는 프로그램을 만들기
# randint() 함수를 검색하여 사용법을 익힌 후 프로그램을 작성하세요

from random import *

# randint(a, b) 함수는 a부터 b까지의 사이에 있는 정수를 반환해주는 함수
num = randint(1, 6)
print("주사위 눈 : " , num)

# rondom() 함수는 0.0 부터 1.0 미만의 임의의 값을 float형태로 반환해주는 함수
num = random()
print("num : ", num)

# randrange(start, stop, step) 함수는 start에서 stop까지 step의 값에 따라서 임이의 수를 반환해주는 함수
num = randrange(0, 101, 2)
print("num : ", num)

# randrange(a)(메소드 오버로딩) 함수는 0에서무터 a미만까지의 임의의 정수값을 반환하는 함수
num = randrange(10)
print("num : ", num)



# randint(a, b) 함수는 a부터 b까지의 사이에 있는 정수를 반환해주는 함수
num1 = randint(1, 6)
print("주사위 눈 : " , num1)

if num1 == 1:
    print("주사위 눈 : ", num1)
elif num1 == 2:
    print("주사위 눈 : ", num1)
elif num1 == 3:
    print("주사위 눈 : ", num1)
elif num1 == 4:
    print("주사위 눈 : ", num1)
elif num1 == 5:
    print("주사위 눈 : ", num1)
else:
    print("주사위 눈 : ", num1)