
# 사용자로부터 임의의 개수를 입력받아서 합계와 평균을 계산후
# 출력하는 프로그램을 작성해보시오. 단, 센티널은 음수의 값을 사용하시오.

cnt = 0
hap = 0
score = 0

print("종료허실려면 음수를 입력하세요(-1)")
while score >= 0:
    score = int(input(str(cnt+1)+"번째 성적을 입력하시오 : "))
#     음수값인지 검사하는 코드
    if score >= 0:
        hap += score        # 성적의 합을 구하는 코드
        cnt += 1            # 학생의 수를 누적하는 코드

# 합계와 평균을 구하는 코드
if cnt > 0:
    averge = hap/cnt

# 합계와 평균을 출력하는 코드
print(str(cnt)+"명의 학생의 평균은 %d이다." %hap)
print(str(cnt)+"명의 학생의 평균은 %.1f이다." %averge)
