
# 1번을 누르면 10 증속, 2번 10 감속, 3번 플래그변수 이용하여 중지
# 사용자의 입력을 받아서 1,2,3

run = True
k = 0

while run:
    button = int(input("1번을 누르면 10 증속, 2번 10 감속, 3번 중지 : "))
    if button == 1:
        k+=10
        print("속도를 증가시킵니다. +10, 현제속도 : ", k)
    elif button == 2:
        k -= 10
        if k < 0:
            print("속도가 -일 수 없습니다. 다시 시작할까요?")
            k = 0
        else:
            print("속도를 감소시킵니다. -10, 현제속도 : ", k)
    elif button == 3:
        print("중지되었습니다.")
        run = False
    else:
        print("잘못된 입력값입니다. ")
