
# 사용자로부터 출력하고 싶은 구구단을 출력하는 프로그램을 만들기

dan = int(input("정수를 입력하세요 : "))

for i in range(1, 10):
    # 사용자의 잘못된 입력을 걸러내는 방법
    if (dan > 1)or(dan < 10):
        print("단을 잘못 입력하셨습니다. ")
        break
    print(dan, "*", i, "=", dan * i)

