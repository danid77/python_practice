

# 한사람이 돈이 5000 있는데 사탕의 가격이 120원 이라면 최대로 살 수 있는 사탕의
# 수는 몇개인지 알아보는 프로그램

myMoney = 5000
candy = 120

numCandy1 = myMoney/120    # 실수
numCandy2 = myMoney//120   # 정수
print("살 수 있는 사탕의 갯수는?? : ", numCandy1)
print("살 수 있는 사탕의 갯수는?? : ", numCandy2)

# round() : 소수 첫째 자리에서 반올림
print("살 수 있는 사탕의 갯수는?? : ", round(numCandy1))

# 최대로 살 수 있는 사탕을 구입하고 남은 돈
change = myMoney%candy
print("최대로 살 수 있는 사탕을 구입하고 남은 돈 : ",change)