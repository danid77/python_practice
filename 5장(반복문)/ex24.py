
# 입력받은 문자열의 모든 공백을 제거한 문자열을 출력하는 프로그램을 작성하시오.

statements = input("원하는 문자열을 입력하세요 : ")
result = ""

for ch in statements:
    if ch !=" ":    # 공백이 아니라면
        result += ch # result에 하나씩 더해준다.

print("입력한 문자열 : " + statements)
print("공백을 제거한 문자열 : " + result)