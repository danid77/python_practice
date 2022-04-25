# 사용자로부터 상품금액을 입력 받아서 상품의 총 가격을 계산하는 프로그램
# 사용자가 몇개의 상품을 살지 모르니 무한 루프를 이용하고 사용자가 "끝"이라고 입력하면 프로그램 종료

from operator import *

cnt = 0
hap = 0     #상품합계
price = ""   # 각각의 상품 금액

while True:
    price = input("가격을 입력하세요(끝을 입력하면 종료됨) : ")

    if eq(price, "끝"): # eq : 문자열 비교 함수 (price == "끝"과 같은 의미)
        print("총상품 갯수 : "+str(cnt) + ", 총 가격 : ", hap)
        break

    hap += int(price)
    cnt += 1
