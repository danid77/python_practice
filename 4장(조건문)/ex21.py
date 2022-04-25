
# 학점을 세부적으로 나누는 프로그램 만들기
# 조건 
# 1. 사용자로부터 정붓를 입력 받는다.
# 2. 점수가 95  - 100 A+
# 3. 점수가 90  - 94 A0
# 다른 학점도 동일 적용
# F는 그냥 출력

score = int(input("점수를 입력하세요 : "))
grade = ""  # 초기화
print("입력한 점수 : ", score)

if score >=90:
    if score >= 95:
        grade = "A+"
    else:
        grade = "A0"
elif score >=80:
    if score >= 85:
        grade = "B+"
    else:
        grade = "B0"
elif score >=70:
    if score >= 75:
        grade = "C+"
    else:
        grade = "C0"
elif score >=60:
    if score >= 5:
        grade = "D+"
    else:
        grade = "D0"
else:
    grade = "F"

print("당신의 점수는 ", score,"이며 당신의 점수는 ", grade, "입니다.")