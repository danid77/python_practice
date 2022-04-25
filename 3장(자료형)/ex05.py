



#문자열의 연결
# +연산자는 문자열 사이에 들어가면 문자열을 연결해주는 역할을 한다.
first_name = "Eun Hyuk"
last_name = "shin"
name = last_name + first_name
print(name)

# temp = "person" + 100 --> 에러 : 문자의 접합이 잘못됨
# 파이썬에서는 모든 데이터에서는 데이터 타입이 존제한다. 위의 소스코드에서 확인을 하면
# "Person"은 문자열, 100은 int(float) 타입이다. 때문에 타입일치가 되지 않아 오류가 발생

# 해결하기 위해서 타입을 일치시킨다.
temp = "person" + str(100)
print(temp)

# 문자열을 숫자로 변환
price = "123456"
print(type(price))
price = int("123456")
print(type(price))

#실수 일때는 float()를 사용하면 된다.
price = float("123456.001")
print(type(price))

# 문자열의 반복
# 문자열에서 * 연산자를 사용하면 그만큼 반복이 된다.
arrow = "->" *10
print(arrow)

arrow = "->"
print(arrow * 10)

# %s(형식 지정자)
# %s(형식 지정자)는 문자열이나 숫자값을 변수에 대입해서 자주 변경이 있는 경우 이런 현식을 지정하여
# 상황에 맞게끔 출력 하도록 하면 된다.
price = 1000    # 정수
print("가격 : %s", "가나") # 문자의 연결형태로 출력됨
print("가격 : %s" %price)

time = "13:49"  #문자열
print("g현제 시간은 : %s" %time)

# %s를 2개이상을 사용하고자 할때는 해당하는 %s의 개수 만큼 소괄호로 묶어서 형식 지정자에 대입해줘야 한다.
temp = "현제 시간은 %s시 %s분 %d초 이다."
print(temp%(10, 35, 33))



