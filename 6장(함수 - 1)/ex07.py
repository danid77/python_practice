
# 함수가 리턴값이 없는 경우에 대한 예제
def printInfo(name, age):
    print("==================")
    print("이름" + name)
    print("나이", age)
    print("==================")
    return # 여기서는 없어도 상관 없는데 있으면 함수의 끝을 의미함
            #리턴값이 존재하징 않는다면, return뒤에 아무수직을 넣지 않으면 된다.

end_Input = "y"

print("이름과 나이를 입력해주세요.")
while True:
    if end_Input == "n" :
        print("입력을 종료합니다. ")
        break
    elif end_Input == "y":
        name = input("회원의 이름을 입력해주세요 : ")
        age = int(input("회원님의 나이를 입력해주세요 : "))
        printInfo(name, age)

    end_Input = input("계속 입력하시겠습니까?(y or n)")