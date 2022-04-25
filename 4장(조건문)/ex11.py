
# 문자열의 중앙에 잇는 문자를 추출해서 출력을 하는 프로그램을 만들기
# 예를 들어 문자열이 "weekday"라면 중앙의 문자는 "k"가 된다.
# 하지만, 만약 문자열이 짝수 개의 문자를 가지고 있다면 중앙에 문자를
# 2개의 문자를 출력한다. 예를 들어서 "monday"라면 "nd"를 출력하는프로그램

str_1 = input("문자열을 입력하세요 : ")
lenght = len(str_1)

if (lenght % 2) == 1:       # 홀수
    char = str_1[lenght//2]
    print("중앙에 있는 한 글자는", char)
else:
    ch1 = str_1[lenght//2 - 1]
    ch2 = str_1[lenght//2]
    print("중앙에 있는 두 글자는 : ", ch1, ch2)