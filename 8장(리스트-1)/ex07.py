
# 리스트 일치 검사를 하는 실습
# 리스트가 일치하는 연산을 위해서 반드시 2개의 리스트가 반드시 동일한 자료형이어야 한다.(중요)

li1 = [10,20,30]
li2 = [10,20,30]
print(li1 == li2)

li1 = [10,20,30]
li2 = [15,20,30]
print(li1 == li2)

# == 연산자는 2개의 리스트의 길이가 서로 다르면 무조건 False이다.
li1 = [10,20,30]
li2 = [15,20]
print(li1 == li2)

li3 = [4,4,5]
li4 = [4,4,2]
print(li3 == li4)
print(li3 > li4)
print(li3 < li4)

# 아래리스트는 >,<를 비교 할때 아스키코드를 비교한다.
li5 = ["a","b","c"]
li6 = ["a","b","d"]
print(li5 > li6)
# ord("값") 메소드는 값의 아스키코드를 구해준다.
print(ord("c"))
print(ord("d"))
# chr(값)메소드는 아스키코드를 문자로 변환해준다.
print(chr(100))
print(chr(97))
print("================================")

# 리스트 정렬하기 2가지 방법
# 1. 리스트객체의 sort()메소드를 이용하는 방법
# 원본 리스트의 값이 변경이 된다. 그리고 리턴값이 없다.
li = [80,90,100,-70,-30]
print(id(li))
li.sort()
print(li)
print(id(li))
print("================================")

# 2. 내장함수로 존재하는 sorted() 메소드를 이용하는 방법
# 원본리스트는 그대로 유지하고 정렬된 리스트를 반환한다.
li = [80,90,100,-70,-30]
c_li = sorted(li)
print(li)
print(id(li))
print(c_li)
print(id(c_li))
print("================================")

# 리스트 객체의 reverse()는 내림차순이 아니라 리스트 요소를 뒤집는 메소드
li = [80,90,100,-70,-30]
li.reverse()
print(li)
# reverse 매개변수의 값을 True로 설정하면 내림차순 정렬이 이루어진다.
li.sort(reverse=True)
print(li)
print("================================")

# sorted()의 내림차순 정렬
li = [80,90,100,-70,-30]
c_li = sorted(li, reverse=True)
print(li)
print(c_li)
print("================================")

# 문자열 정렬하기(유니코드를 기준으로 정렬을 한다.)
# 뒷부분에 인코딩 디코딩 부분을 강의할 때 자세하게 설명하도록 한다.
li = ["서울","런던","뉴욕","파리","뮌헨"]
li1 = sorted(li, key=str.lower)
print(li1)
print("================================")

# 긴 문자열을 분리하는 방법(split() : 문자열을 분리해서 리스트 타입으로 반환하는 메소드)
statement = "나는 한국에서 살고있는 개발자 입니다. 만나서 반갑습니다."
li_s1 = statement.split()
print(li_s1)
li_s2 = statement.split(".")
print(li_s2)