
# 일회용 패스워드 생성기를 이용하여 3개의 패스워드를 생성하여 출력하는 프로그램 만들기
# 페스워드의 길이는 6개로 한정한다.
# 난수가 발생되는 범위값을 지정을 아래와 같이 한다.
# 난수 발생문자열 : "

import random

def get_password():
    num_str = "0123456789"  #문자열
    password = ""

    for i in range(6):
        index = random.randrange(len(num_str))  #0~9까지의 범위
        password = password + num_str[index]    #인덱스 적용
    return password

print("본인인증을 위해서 발송한 숫자를 입력하세요 : ", get_password())
print("본인인증을 위해서 발송한 숫자를 입력하세요 : ", get_password())
print("본인인증을 위해서 발송한 숫자를 입력하세요 : ", get_password())
print("본인인증을 위해서 발송한 숫자를 입력하세요 : ", get_password())