# 리스트의 기초연산들 실습하기

# 요소를 삽입하기
# append() 메소드 : 리스트 요소의 항상 마지막 끝에 추가 된다.
# insert() 메소드 : 리스트명.insert(인덱스, 추가할 요소), 원하는 인덱스에 요소를 추가할 수 있다.
li1 = ["Tv", "오디오", "PC", "키보드"]
print("li1의 주소 :", id(li1))

# append() 사용
li1.append("마우스")
print("li1의 주소 : ", id(li1))
print(li1)

# insert() 사용하여 원하는 인덱스에 요소 추가, 뒤에 요소들은 한 칸씩 밀려났다.
li1.insert(1, "휴대폰")
print("li1의 주소 : ", id(li1))
print(li1)

# 리스트에서 요소 찾기
# in, not in 연산자들은 리스트에 요소가 존재하는지 확인하는 용도
hero = ["스파이더맨", "아이언맨", "슈퍼맨", "캡틴아메리카", "블렉위도우", "닥터스트레인지"]
if "아이언맨" in hero:
    print("아이언맨이 존재합니다.")
else:
    print("아이언맨이 존재하지 않습니다.")

# 리스트에서 요소를 찾을때 해당 요소의 인덱스를 알고자 한다면 index()를 사용하면 된다.
# 아래와 같이 list에 해당하는 값이 존재하지 않으면 index()는 에러를 발생시킨다.
# 하여, 조건절과 in, not in 연산자를 이용하여 존재하는지 확인을 먼저하는 습관을 들이도록 한다.
if "아이언맨" in hero:
    index = hero.index("아이언맨")
    print("아이언맨의 인덱스 : ",index)
else:
    print("아이언맨이 존재하지 않습니다.")

# 리스트서 요소를 삭제하는 방법 - pop(),remove()
# 1. 리스트명.pop(인덱스), 리스트에서 인덱스에서 해당하는 요소를 삭제한 후, 요소를 반환한다.
# 2. 리스트명.remove("요소"), 리스트에서 인덱스에서 해당하는 요소가 있으면 삭제한 후, 요소를 반환하지 않는다.
# 3. del 리스트명[인덱스], 리스트에서 인덱스에서 해당하는 요소가 있으면 삭제한 후, 요소를 반환하지 않는다.

hero = ["스파이더맨", "아이언맨", "슈퍼맨", "캡틴아메리카", "블렉위도우", "닥터스트레인지","슈퍼맨"]
element = hero.pop(0)
print("element : ", element)
print("hero : ", hero)

# remove() 메서드는 리스트의 요소중 중복된 요소가 존재한다면 인덱스가 작은 요소를 먼저 제거한다.
element = hero.remove("슈퍼맨")
print("element : ", element)
print("hero : ", hero)

# remove() 메서드와 반복문을 이용해서 다수의 같은 값을 제거 할 수 있다.
hero1 = ["스파이더맨", "아이언맨", "슈퍼맨", "캡틴아메리카", "블렉위도우", "닥터스트레인지","슈퍼맨"]
print(hero1)
value = "슈퍼맨"
while value in hero1:
    hero1.remove(value)

print(hero1)

# del 키워드로 요소를 삭제하기
hero = ["스파이더맨", "아이언맨", "슈퍼맨", "캡틴아메리카", "블렉위도우", "닥터스트레인지","슈퍼맨"]
# print(del hero[4])    오류
# element = del hero[4] 오류
del hero[4]
print(hero)

del hero[2:3]
print(hero)

del hero[:]
print(hero)

# clear() : 리스트의 모든 요소를 삭제하는 메소드
hero = ["스파이더맨", "아이언맨", "슈퍼맨", "캡틴아메리카", "블렉위도우", "닥터스트레인지","슈퍼맨"]
element = hero.clear()
print(element)
print(hero)

# 리스트에 포함된 특정 요소의 갯수를 알고자 할때, count()를 이용하면 된다.
hero = ["스파이더맨", "아이언맨", "슈퍼맨", "캡틴아메리카", "블렉위도우", "닥터스트레인지","슈퍼맨"]
cnt = hero.count("슈퍼맨")
print(cnt)

# +=
li1 = [1,2,3]
li2 = [10.1,11.3]
li1 += li2
print(li1)
# extend(list 타입의 매개변수)는 리스트를 더하는 함수(+=와 동일한 효과)
li1.extend(li2)
print(li1)