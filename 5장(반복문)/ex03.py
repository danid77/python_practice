
# 사용자가 입력한 수 num까지 합계를 구하는 프로그램을 for문을 이용해서 작성하시오.

hap = 0
num = int(input("숫자를 입력하세요 : "))

for i in range(num + 1):
    hap += i
print("합은 : ", hap)