
# 반복문으로 문자열 관련 처리하기 학실습
fruit = "apple"

# fruit문자열 변수에 값을 하나씩 문자형태로 가져와서 출력하는 코드
for letter in fruit:
    print(letter,end=" ")
print("")
print("------------------------------")
# 사용자로 부터 문자열(영문)을 입력 받아서 모음을 전부 없애는 코드
s= input("문자열을 입력하세요(영문자) : ")

# 영문자 모음의 문자열
vowels = "aeiouARIOU"
result = ""
for letter in s:
    # s의 값을 하나씩 아래의 if문에 전달
    # 하나씩 반복하는 문자가 모음 문자열에 존재하지 않는다면... 참을 반환
    if letter not in vowels:
        result += letter
print("자음만 출력 : ", result)


# 문자열을 입력 받아서 자음과 모음의 갯수를 집계하는코드
original = input("문자열을 입력하세요(영문자) : ")
# 입력받은 문자열을 전부 소문자로 변경한다.
word = original.lower()     # 대문자로 바꾸는 함수 : upper()
vowels = 0
consonanats = 0

# 문자열의 길이가 0초과하고, 알파벳이라면... 참을 반환한다.
if len(original) > 0 and original.isalpha():
    for ch in word:
#         루프변수의 값이 모음에 해당하면...
        if ch in "aeiou":
            vowels +=1
        else:           # 자음이라면...
            consonanats +=1

print("모음의 개수 : ", vowels)
print("자음의 개수 : ", consonanats)