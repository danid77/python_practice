
# 사용자로부터 태어난 연도를 입력 받아서 학생의 초등학생, 중학생, 고등학생, 대학생 분류 중에서 어디에 해당하는지 출력하는
# 프로그램을 작성해보세요

year = int(input("태어난 년도를 입력하세요 : "))
age = (2022 - year) + 1

print("현제 나이 : ", age)

if age < 8:
    print("영유아")
elif (age > 7)and(age < 14) :
    print("초등학생")
elif (age > 13)and(age < 17) :
    print("중학생")
elif (age > 16)and(age < 20) :
    print("고등학생")
elif (age > 19)and(age < 28) :
    print("대학생")
else:
    print("일반인")

