
# 몸무게d와 키를 입력받고 BMI가 20.0이상이고 25미만 이면 표준이고 아니면 체중관리가 필요합니다.
# 라고 출력하는 프로그램 만들기
# 키를 입력받고 100.0으로 나누고 공식에 대입한다.
# BMI = 몸무게 / (키 * 키)

height = float(input("키를 입력하세요 : "))
weight = float(input("몸무게를 입력하세요 : "))

height /= 100.0 # height = height / 100.0 : 복합연산자

bmi = weight/(height*height)

if(bmi >= 20.0) and (bmi < 25):
    print(str(bmi) + " 표준입니다. ")
else:
    if bmi < 20.0:
        print(str(bmi) + " 저체중 - 체중관리 필요")
    else:
        print(str(bmi) + " 과체중 - 체중관리 필요")
