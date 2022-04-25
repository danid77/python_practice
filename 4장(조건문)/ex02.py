
# 조건문 if문만 사용

score = 99

# 몇 십개의 if구문이 존재하더라고, CPU는 모든 if문을 참조한다.
# 그러므로 애플리케이션 프로그램의 성등은 떨어질 수 밖에 없다.
if score >= 90:
    print("학점은 A등급입니다.")

if score >= 80:
    print("학점은 B등급입니다.")

if score >= 70:
    print("학점은 C등급입니다.")

if score >= 60:
    print("학점은 D등급입니다.")