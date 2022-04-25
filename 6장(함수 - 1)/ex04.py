
# 섭씨 온도를 화씨 온도로 반환하여 반환하는 함수 FtoC()를 작성하시오.
# 공식 : F = (9.0/5.0)*C+32

def main():
    # FtoC 함수 호출
    print("F : ", temp_f, "-> C :", round(FtoC(temp_f), 2))

temp_f = float(input("화씨온도를 입력해주세요 : "))

# 인터프리터가 함수 선언 확인
def FtoC(temp_f):
    temp_c = (5.0 * (temp_f - 32))/9.0
    return temp_c

# 메인 메소드 호출
main()
