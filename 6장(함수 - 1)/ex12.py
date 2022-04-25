
# 사용자로부터 10진수를 입력받아서 2진수 문자열로 변환하여 반환하는
# 함수 decTobin(num)를 작성하세요

def decTobin(num):
    binary = ""

    while num != 0 :
        value = num % 2
        if value == 0:
            binary = "0" + binary
        else:
            binary = "1" + binary
        num//= 2
        # print("num : ", num)
    return binary

decNum = int(input("10진수를 입력하세요 : "))
print("10진수가 ", decNum, "일때 2진수는 ", decTobin(decNum),"이다.")

print("--------------------------------------")
# 파이썬에서 제동하는 진법 변환 함수들
print("내장함수 2진수 변환 함수 : ", bin(decNum))      #2진수로 변환하는 내장함수
print("내장함수 8진수 변환 함수 : ", oct(decNum))      #8진수로 변환하는 내장함수
print("내장함수 16진수 변환 함수 : ", hex(decNum))      #16진수로 변환하는 내장함수

print("--------------------------------------")
# 2진수, 8진수, 16진수의 값을 10진수로 변환하는 방법
print(int("0b1010", 2))
print(int("0o12", 8))
print(int("0xa", 16))