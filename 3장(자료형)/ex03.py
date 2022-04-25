from math import *

# 다중 판매기를 시물례이션하는 프로그램을 사용자는 1000원 지폐와
# 500원, 100원 동전을 사용할 수 있다. 물건 값을 사용자로 부터 입력 받아서
# 1000dn, 500, 100원 짜리 돈의 갯수를 입력하면 거스름돈을 계산하여 동전으로
# 반환하는 프로그램

itemPrice = int(input("물건 값을 입력하세요 : "))
bills_1000 = int(input("1000원 갯수 입력 : "))
coin_500 = int(input("500원 갯수 입력 : "))
coin_100 = int(input("100원 갯수 입력 : "))

#거스름돈 구하기
nod_money = ((bills_1000 * 1000) + (coin_500 * 500) + (coin_100 * 100)) - itemPrice

# 거스름돈 (500원 동전 갯수)를 계산
nCoin500 = nod_money // 500
nod_money = nod_money % 500     # 500원으로 나눈 나머지

# 거스름돈 (100원 동전 갯수)를 계산
nCoin100 = nod_money // 100
nod_money = nod_money % 100     # 100원으로 나눈 나머지

# 거스름돈 (50원 동전 갯수)를 계산
nCoin50 = nod_money // 50
nod_money = nod_money % 50     # 50원으로 나눈 나머지

# 거스름돈 (10원 동전 갯수)를 계산
nCoin10 = nod_money // 10
nod_money = nod_money % 10     # 10원으로 나눈 나머지

# 거스름돈 (1원 동전 갯수)를 계산
nCoin1 = nod_money

print("거스름돈 : ",nod_money)
print("500 :", nCoin500, "\n100 : ", nCoin100, "\n50 : ", nCoin50, "\n10 : ", nCoin10, "\n1 : ", nCoin1)