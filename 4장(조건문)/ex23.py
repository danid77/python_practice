
# 사용자 로부터 연도를 입력 받고 윤년인지 아닌지 판단하는 프로그램을 만들기
# 윤년의 조건
# 1. 연도가 4로 나누어 떨어지면 윤년이다.
# 2. 100으로 나누어 떨어지는 연도는 제외한다.
# 3. 400으로 나누어 떨어진 연도는 윤년이다.

year = int(input("년도를 입력하세요 : "))

if ((year%4) == 0 and (year%100) != 0) or (year%400) == 0:
    print(year, "년은 운년입니다. ")
else:
    print("운년이 아닙니다. ")
