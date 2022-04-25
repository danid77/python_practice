# 문자열의 인덱싱
# 인덱싱이란 문자열에서 문자를 추출하는데 문자열에는 각각의 해당하는 문자에 번호(인덱스)가 존제한다.
# [인덱스]라 하면 문자열에서 문자를 추출할 수 있다.
# 인덱스라 함은 무조건 0부터 시작 된다. 마지막 인덱스는 n-1이 성립 된다.
# 파이썬 특수기능인 인덱스를 처리 할떄 음수도 사용이 가능하다(-6 -5 -4 -3 -2 -1)

word = "hello"
print(len(word))

print(word[0])
print(word[3])

# 끝의 글자를 알고 싶으면 이렇게 사용 해도 된다.
print(word[len(word)-1])

# print(word[10]) 에러 : 해당하는 인덱스가 없음 (IndexError: string index out of range)

# 파이썬에서는 한 번 작성된 문자열은 변경이 불가능 하다.
# word[3] = 'f' 에러 : TypeError: 'str' object does not support item assignment
# 인덱스 값 변화 불가(참고로 다른 언어는 가능)

# 사용자로부터 문자열을 입력을 3개 받도록 한다. 각 해당 문자열의 첫번쨰 문자를 인덱싱하여
# 문자를 합쳐서 문자열로 만드는 프로그램을 만들어 보자.
item1 = input("첫번째 단어를 입력하세요 : ")
item2 = input("첫번째 단어를 입력하세요 : ")
item3 = input("첫번째 단어를 입력하세요 : ")

word = item1[0] + item2[0] + item3[0]
print("새로만든 문자열 : "+word)