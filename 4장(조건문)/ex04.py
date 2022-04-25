
# bool 변수 알아보기
# 부울변수의 용도는 플래그 변수 형태로 사용을 많이 한다.
# 타 프로그래밍 언어에서는 부울 변수의 값은 소문자로 시작하는 ture, false를 사용하지
# 만 파이썬은 대문자로 시작하는 Ture, False를 사용한다.

flag = True
print(type(flag))
print(flag)

# flag = !flag 타언어에서 !는 부정문, 파이썬은 not을 붙인다.
flag = not flag
print(type(flag))
print(flag)

if flag :
    print("참입니다.")
else :
    print("거짓입니다.")
    flag = not flag

if flag :
    print("참입니다.")
else :
    print("거짓입니다.")
    flag = not flag