
# for문을 이용해서 팩토리얼(n!)을 계산하는 프로그램

fact = 1.0
n = int(input("숫자를 입력하세요. : "))

for i in range(1, n+1):
    # TypeError: 'float' object cannot be interpreted as an integer
    #  range는 정수형만을 인자로 받습니다. 따라서 실수는 처리할수가 없는 것이죠.
    fact *= i

print(n, "!은", fact, "입니다.")

