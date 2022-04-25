from random import *
# 임의의 숫자를 발생시켜 숫자를 맞추는 프로그램

cnt = 0     # 횟수
num = randint(1,100)
print("발생한 난수의 값 : ", num)

print("1부터 100사이에 숫자를 맞추어 보세요(단 기회는 7번)")

while cnt < 8:
    guess = int(input("숫자를 입력하세요 : "))
    cnt += 1

    if guess < num:
        print("업")
    elif guess > num:
        print("다운")
    elif guess == num:
        print("정답! 시도횟수 : ", cnt)
        code = input("게임을 계속하시겠습니까?? : y = 계속 , n = 끝")
        if code == "n":             # 게임종료 코드
            print("게임을 종료합니다.")
            exit()
        else:                       # 게임 재시작 코드
            print("-------------------------------------")
            print("게임을 재시작합니다.")
            # 난수 초기화, 카운트 초기화
            num = randint(1, 100)
            print("발생한 난수의 값 : ", num)
            cnt = 0

print("fallㅠㅠ")