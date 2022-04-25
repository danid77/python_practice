
# 입력받은 문자열을 거꾸로 출력하는 프로그램을 작성하시오.
print("for문")
statements = input("원하는 문자열을 입력하세요 : ")
result = ""

for ch in statements:       # 안녕하세요
    # '='는 가장 마지막에 계산됨
    result = ch + result
# 1.   안       안 + ""
# 2.   녕안     녕   안
# 3.   하녕안    하   녕안
# 4.   세하녕안  세    하녕안
# 5.   요세하녕안 요    세하녕안
print("입력한 문자열 : " + statements)
print("역순 문자열 : " + result)

print("------------------------------------------")
print("lsit() 함수는 문자열을 리스트 타입으로 바꾸는 함수이다. ")
s_list = list(statements)
# print(type(s_list))
# reverse()는 리스트 타입만 역순으로 바꿔주는 함수이다.
s_list.reverse()
# join() 함수는 역순으로 된 문자열을 연결해서 출력을 하고 있는 코드드print("".join(s_list))
print("".join(s_list))

s1 = statements
# reversed()는 문자열만 역순으로 바꿔주는 함수이다.
print("".join(reversed(s1)))

# reverse()는 리스트 타입만 역순으로 바꿔주는 함수이다.
# reversed()는 문자열만 역순으로 바꿔주는 함수이다.
# 차이 비교

# 파이썬에서는 [::-1]를 사용해서 문자열을 역순으로 출력할 수 있다.
print("--------------------------------------")
print(statements[::-1])

# 문자열 3번째 인덱스 부터 역순으로 출력하는 방법이다.
print("--------------------------------------")
print(statements[3::-1])