# str 클래스의 메서드 실습
# split() : 문자열에서 단어(토큰)을 분리하고자 할 때 사용하는 메서드이다.
# 인자값으로 구분자(seperator)를 주게 되면 주어진 구분자로 문자열을 분리한다.
# 기본 인자값 공백(스페이스바)이다.
string = "안녕 john 난 지금 학교 가고 있어"
li1 = string.split()   # 공백으로 분리
print(type(li1))
print(li1)
print("--------------------")

# split() 구분자를 하나밖에 받지 않는다.(자바는 허용)
string = "안녕,john,난,지금,학교,가고,있어"
li2 = string.split(",")   # 콤마로 분리
print(li2)

string = "안녕/john,난|지금&학교,가고,있어"
li2 = string.split(",/|&")  #분리 안됨
print(li2)
print("--------------------")

# 정규표현식을 사용하기 위해서 regex 모듈을 인스톨 하자
import regex
string = "안녕/john,난|지금&학교,가고,있어"
# regex.split("[분리기호 인자값들", 대상자)
li3 = regex.split("[/,|&]", string)   # 정규표현식으로 분리
print(li3)
print("--------------------")

# 문자열을 검사
string = "abcd"
print("영문자 인가? : ",string.isalpha())    # 문자열이 영문자인지 확인하는 코드
print(string.isalpha())
print("--------------------")

string = "12345"
print("숫자 인가? : ",string.isdigit())    # 문자열이 10진수인지 확인하는 코드
print(string.isdigit())
print("숫자 인가? : ",string.isdecimal())    # 문자열이 10진수인지 확인하는 코드
print("----------------------------")

string = "abcd12345"
print(string.isdigit())     # false
print(string.isalpha())     # false
# 슬라이스로 범위를 지정해서 부분적으로 판별 가능
print(string[5:10].isdigit())     # True
print(string[0:4].isalpha())     # True

print("----------------------------")

string = "abcd12345"
print(string.isalnum())    # 문자열이 영문자, 숫자인지 동시에 확인하는 코드
print("----------------------------")

string = "½"
# numeric 굉장히 넓은 의미인데, 숫자값 표현에 문자열을 인정해준다.
print(string.isnumeric())
# str 클래스에서 음수, 실수 판별하는 메서드는 없다.
# 음수, 실수 판별할려면 함수를 만들어서 사용 할 수밖에 없다.

print("----------------------------")
string = "   "
print(string.isspace())   # 공백인지 확인하는 것




# 부분 문자열 검색 실습
print("----------------------------")
# string = input("파이썬 소스를 입력해주세요 : ")

# endswith(문자열) 메소드는 인자값 문자열로 '끝'이 나면 True 리턴한다.
string = ".py"
if string.endswith(string):
    print("올바른 파일이름입니다.")
else:
    print("틀린 파일이름입니다.")

print("----------------------------")


string = "2021-03-04.txt"
# startswith(문자열) 메소드는 인자값이 문자열로 '시작'하면 True 를 리턴한다.
if string.startswith("2021"):
    print("2021년 파일입니다.")
else:
    print("2021년 파일이 아닙니다..")

print("----------------------------")
# string = input("영어단어를 입력하세요 : ")
string = "Hi! Jin. How are you today? You must go Center"
string_s = "hi! Jin. How are you today? You must go Center"
print("대문자로 변경 : ",string.upper())    # 대문자로 변경
print("소문자로 변경 : ",string.lower())    # 소문자로 변경
print("앞 한글자만 대문자로 변경 : ",string_s.capitalize())    # 앞 한글자만 대문자로 변경
print("앞 한글자만 대문자로 변경 : ",string_s.title())         # 앞 한글자만 대문자로 변경


print("----------------------------")
# format() 메소드는 포맷 {}을 만들어놓고 문자열을 생성하는데 사용하는 것이다.
string = "{}b{}"
print(string.format("a","c"))

print("----------------------------")
# join()는 리스트 같은 반복(iterable) 인자를 전달받아서 문자열로 연결하는데 사용
string = ["a", "b", "가"]
print("!".join(string))
string = ["안녕", "반가워", "잘가", ""]
print(". ".join(string))

print("----------------------------")
# partition() 전달받은 인자값으로 문자열을 튜플 형태로 나눈다. 그러므로 리턴타입은 튜플이다.
string = "eunhyuk@gmail.com"
print(string.partition("@"))

print("----------------------------")
# count()는 인자값으로 들어오는 값을 문자열에서 몇 개 있는지 카운팅을 해준다.
# 찾는 인자값이 없다면 0을 리턴해준다.
string = "aaaaaabcc"
print("a의 갯수",string.count("a"))
print("찾는 인자값이 없는 경우 : ",string.count("z"))

string = "안녕하세요 안녕 안경 안줌 안이"
print(string.count("안"))

print("----------------------------")
# find()메소드는 특정 첫 단어만 찾아서 인덱스를 리턴하고 없다면 -1을 리턴한다.
# find()메소드는 index()과 비슷하다.
# 두 개의 차이점은 특정 단어를 찾으면 인덱스를 리턴하는건 동일하지만,
# 없다면 index() 에러를 발생시키고
# find()는 -1을 리턴하고 에러는 발생시키지 않는다.

string = "apple"
print("fine의 리턴값 : ",string.find("p"))
print(string.find("z"))
print(string.index("p"))
# print(string.index("z")) ValueError: substring not found

print("----------------------------")
# 문자열에서 공백을 제거하는 방법
# strip() : 양쪽 공백, 탭문자, 줄바꿈(enter)도 제거
# lstrip() : 왼쪽 공백만 제거(탭키 포함)
# rstrip() : 오른쪽 공백만 제거(탭키 포함)

string = "\t      aaaaa  bbbbb   ccccc    ddddd     \t"
print(string.strip())
print(string.rstrip())
print(string.lstrip())

# 단 메소드로 문자열 중간에 존재하는 공백은 제거할 방법이 없다.(함수를 만들어서 직접 사용해야 한다)


