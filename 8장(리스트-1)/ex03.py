
# 리스트 다양한 데이터를 저장할 수있다고 배웠다.
# 하지만 현업에서는 같은 종류(모델)의 같은타입의 데이터를 저장하면서 사용한다.

# 리스트는 문자열도 저장 할 수 있다.
# 사용자로부터 강아지의 이름을 저장하였다가 출력하는 프로그램을 작성해라

dog_name = []

while True:
    dog = input("강아지 이름을 입력하세요(종료시에 엔터키를 누르시오.) : ")
    dog_name.append(dog)
    if dog == "":
        break
# if 문이 먼저오면 ""도 리스트에 추가된다.
# ['ㅡㅐ흐ㅐㅎ', 'danid', 'tom', 'all', '']이런식으로 출력됨
print("강아지의 이름들은 ", dog_name, "입니다.")

print("================================================")
print("선생님 풀이")

dogName = []
# 무한루프
while True:
    name = input("강아지 이름을 입력하세요(종료시에 엔터키를 누르시오.) : ")
    # 엔터키를 눌렀을때 루프를 탈출하는 코드
    if name == "":
        break
    dogName.append(name)

print("강아지의 이름들은 ", dogName, "입니다.")