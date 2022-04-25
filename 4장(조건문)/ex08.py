
# 사용자로부터 2개의 정수를 입력 받아서 최대값을 말해주는 포르그램\

x = int(input("첫번째 정수 : "))
y = int(input("두번째 정수 : "))

maximum = 0
if x>y:
    maximum = x
else:
    maximum = y

print("둘중의 큰수 : " + str(maximum))