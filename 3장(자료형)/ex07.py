

# 리스트에 대한 실습
# 리스트의 정의 : 여러개의 값을 모아서 하나의 변수에 저장할 수가 있는 데이터 타입이다.
# 아주 유용하게 얼리 사용된다. 리스트[]안에 값을 저장한다. 

city = ["서울", "부산", "대구", "런던", "파리"]

# 리스트의 길이를 알아 내고 싶을때도 len() 사용 가능
print(len(city))
print(city)
print(city[2])

# 리스트는 아래와 같이 해당하는 인덱스의 값이 변경이 가능한 객체이다.
city[1] = "전주"
print(city)

# 리스트는 정수, 문자열에 국한 되지 않고 여러개의 값을 저장 할 수가 있다. 
temp = ["대구", "부산", 100, 10.798]
print(temp)

# 한사람의 정보를 출력 
name = input("이름 : ")
age = input("나이 : ")
adress = input("주소 : ")
tall = input("키 : ")
wight = input("몸무게 : ")

person = [name, age, adress, tall, wight]
print(person)