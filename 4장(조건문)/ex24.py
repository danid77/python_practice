
from random import *
# 숫자 추측게임을 만들기
rand_num = randint(1, 100)

user_num = int(input("숫자를 맞춰보세요.(1~100) : "))
cnt = 0

while True :
    if user_num == rand_num:
        print("정답!")
        print("시도횟수 : ", cnt)
        break
    elif user_num > rand_num:
        print("다운")
        # 파이썬에서는 ++, -- 이런 증감연산자는 없다.
        cnt += 1
    elif user_num < rand_num:
        print("업")
        cnt += 1
    user_num = int(input("숫자를 맞춰보세요.(1~100) : "))
