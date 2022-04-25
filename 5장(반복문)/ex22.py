
# 사용자로부터 문자열을 입력받아서 알파벳 문자의 갯수, 숫자의 갯수, 스페이스의 갯수를 출력하는 프로그램을 작성하시오

statememts = input("문자열을 입력하세요 : ")
alpha_cnt = 0
digit_cnt = 0
spaces = 0

for ch in statememts:
    if ch.isalpha():    #알파벳이라면
        alpha_cnt+=1
    elif ch.isdigit():  #숫자이라면
        digit_cnt+=1
    elif ch.isspace():  #공백이라면
        spaces+=1
    else:
        print("해당하는 문자는 알파벳, 숫자, 공백이 이닙니다. ")

print("알파벳 문자의 갯수 : ", alpha_cnt)
print("숫자의 갯수", digit_cnt)
print("공백의 갯수", spaces)


