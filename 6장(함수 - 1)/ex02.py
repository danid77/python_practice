
# 정수를 입력받아서 제곱을 구하는 코드



def jam(num):
    i = num**2
    return i

num = int(input("정수를 입력하세요 : "))
print("제곱하기 전 : ", num)
print("제곱 : ", jam(num))