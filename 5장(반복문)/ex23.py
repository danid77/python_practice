# 사용자로부터 전화번호를 입력 받다보면 "-"를 적는 경우가 많다.
# "-"를 합하여 입력 받도록 하고 출력을 할 때는 "-"삭제를 한 문자열을 출력하는 프로그램

phone_num = input("전화번호를 입력하시오")
new_phone_num = ""

if len(phone_num) == 12 or len(phone_num) == 13:
    for phone in phone_num:
    # 루프문자가 "-"가 아니라면 참을 반환한다.
        if phone != "-":
            new_phone_num += phone
    print("'-'을 제거한 전화번호 : ", new_phone_num)
else:
    print("전화번호 입력이 잘못 되었습니다. ")
