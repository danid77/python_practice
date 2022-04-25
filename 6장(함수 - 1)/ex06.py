# 간단한 사칙연산 계산기 만들기

# 더하기 함수
def add(x, y):
    return x + y


# 빼기 함수
def sub(x, y):
    return x - y


# 곱하기 함수
def multiply(x, y):
    return x * y


# 나누기 함수
def divide(x, y):
    return round((x / y), 2)

temp = "y"  # y값으로 설정해야 반복문 안에 elif에 들어갈 수 있다. 

while True:
    if temp == "n":
        break
    elif temp == "y":
        n1 = float(input("첫번째수 : "))
        n2 = float(input("두번째수 : "))
        op = input("원하는 연산 입력 (+ - * /) : ")
        if op == "+":
            print(add(n1, n2))
        elif op == "-":
            print(sub(n1, n2))
        elif op == "*":
            print(multiply(n1, n2))
        elif op == "/":
            print(divide(n1, n2))
        else:
            print("잘못된 계산입니다.")
    temp = input("계산을 계속 하시겠습니까?(y or n) : ")
