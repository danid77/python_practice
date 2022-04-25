


# 문자열에 대한 실습

# 큰 따옴표(double quotation) : 묶으면 문자열이 된다. (왠만하면 이걸로 사용)
welcome = "Happy new Year 2022"
print(welcome)

# 작은 따옴표(single quotation) : 묶으면 문자열이 된다.
welcome = 'Happy new Year 2022'
print(welcome)

# 작은 + 큰 따옴표 : 묶으면 오류. - "의 끝을 찾을 수 없다.
# welcome = "Happy new Year 2022' - 에러

# 큰 따옴표 1개 : 오류. - "의 끝을 찾을 수 없다.
# welcome = "Happy new Year 2022 - 에러

# 아래와 같이 ""안에 ""가 있다면 컴파일러가 혼돈을 일으켜 틀린 문법이기때문에 에러를 발생
# message = "은혁이가 "안녕하세요"라고 인사했습니다."

# ""안에 ''가 있으면 ''를 문자로 인식
message = "은혁이가 '안녕하세요'라고 인사했습니다."
print(message)

# 파이썬에서는 따옴표를 출력하고자 할때, \를 이용한다.
# \가 따옴표 앞에 있으면 ' 는 특수한 의미를 잃어버리고 하나의 문자로 편승되어 문자열을 이룬다.(큰따옴표도 마친가지임)
message = 'doesn\'t'
print(message)

message = "\"yes,\" I can do it."
print(message)

# \n : 줄바꿈
message = "First\nSecond\nThird"
print(message)

# 특수문자 \t는 탭만큼 띄우는 문자이다.
message = "c:\temp\name"
print(message)

# 위의 \t, \n 이런 이스케이프 문자들의 기능을 제거를 시키기 위해서는
# 문자열 시작 앞에 r을 붙여준다.(중요함)
message = r"c:\temp\name"
print(message)

# 문자열(한글이나 영어 상관없이)의 길이를 알고자 한다면 len()함수를 이용한다.
message = "world war 2"
print(len(message))

message = "세종대왕 한글"
print(len(message))