
# 사용자로부터 정수를 입력 받아서 홀수 인지 짝수인지 말해주는 포르그램
num = int(input("정수를 입력하세요 : "))

if (num % 2) == 0 :
    print("짝수 입니다.")
else:
    print("홀수 입니다. ")
    
# not all arguments converted during string formatting : 변수 타입이 맞지 않아서 오류 발생