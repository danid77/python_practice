
# 소수를 판별하는 함수 is_prime()를 작성해보자
# 소수면 true,  아니면 False를 출력하는 함수
# 1과 자기자신과 나누어지는 수를 소수라고 한다.
def is_prime(num):
    for i in range(2, num):
        temp = True
        if (num%i) == 0:
            temp = False
        else:
            temp = True
        return temp

# 함수 호출
num = int(input("정수를 입력하세요 : "))
print(is_prime(num))