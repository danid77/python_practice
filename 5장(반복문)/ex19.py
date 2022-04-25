
# 더블 루프를 이용하여 아래와 같이 출력하는 프로그램을 작성하시오
# 출력결과
#     *
#    ***
#   *****
#  *******

# write = int(input("숫자를 입력하세요"))
print("------------------------------------------")
for i in range(1,6): # 숫자 0일때
    # 공백을 찍는 내부 루프
    for j in range(5-i):
        print(" ", end="")

    # 1, i=2 : 4 -> 1~3까지
    # 1, i=3 : 6 -> 1~5까지
    for j in range(1,i*2):# i가 0일때 문제 생김
        print("*", end="")

    print("")

print("------------------------------------------")
for i in range(1, 11 ,2):
    # 중앙 정렬을 위해서는 ^를 사용한다.
    print("{:^10}".format("*"*i))

print("------------------------------------------")
#     *
#    ***
#   *****
#  *******
#  *******
#   *****
#    ***
#     *

# 위의 삼각형
for i in range(1,6):
    for j in range(5-i):
        print(" ", end="")
    for j in range(1,i*2):
        print("*", end="")
    print("")

# 아래의 역삼각형
for i in range(5):
    for j in range(i):
        print(" ", end="")
    for j in range(10,(i*2)+1, -1):
        print("*", end="")
    print("")

