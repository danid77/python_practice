
# while문의 실습
# while문은 조건을 정해놓고 반복을 하는 구조이다.

i = 0;
while i <5: #조건식이 ture일떄 실행
    print("반갑습니다.")
    i+=1
print("반복이 종료되었습니다.")

# while i <5:
#     print("반갑습니다.")
#     # i+=1 이 코드가 없다면 무한 루프를 돌게 된다.
# print("반복이 종료되었습니다.")

# 숫자 0~9까지 줄바꿈을 하지 않고 출력해보기
i = 0
while i <10:
    print(i, end=" ")
    i+=1

print()
print("-----------------------------------")

# 1~10까지 누계값을 구하시오
i =0
hap = 0

while i <= 10:
    hap += i
    i+=1
print("1~10까지의 누계값 : ", hap)

# 펙토리얼을 구하는 예제
i = 1
fi = 1

while i<6 :
    fi *= i
    i+=1
print("5!의 값은 %d 입니다." %fi)

# 구구단 3단을 출력하는 프로그램
i = 1

while i<=9:
    print("3 * %d = %2d" %(i, 3*i))
    # %2d: % 뒤에오는 숫자들은 출력할때 자릿수를 차자하게끔 만들어준다.
    # %.1f나 %0.1f나 동일한 자리값을 출력한다.(소수점 첫째자리 까지 나타내라.)
    i+=1

# 1 ~100까지의 3의 배수만 누적값을 구하는 예제
i = 1
hap = 0

while i<=100:
    # 3의 배수인지 확인하는 조건
    if(i%3) == 0 :
        hap+=i
    i += 1
print("1~100까지 3의 배수의 합 : ", hap)

print()
print("-----------------------------------")

# 정수 안에 각 자리수의 합을 계산하는 예제
# 예를 들면 1234라면 (1+2+3+4)를 계산하는 것이다..
num = 1234
hap  = 0
while num > 0:
    digit = num % 10    #해당하는 자릿수릐 값을 구하는 코드
    hap += digit
    num //= 10      # num = num // 10 : 10으로 나누어 줌으로써 묷만 num에 저장되는 코드

print("1234정수의 자리수의 합은 %d입니다." % hap)