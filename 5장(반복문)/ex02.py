
# range() 함수 실습하기

# 1. range(x)매개변수 1개짜리 함수 이용
hap = 0
for x in range(10):
    hap+=x  # hap = hap+x

print("1. 0에서 9까지의 누계값", hap)

# 2. range(start, stop)매개변수 2개짜리 함수 이용
# 누적은 하는데 stop값은 포함하지 않는다.
hap = 0
for x in range(0, 10):
    hap+=x  # hap = hap+x

print("2. 0에서 9까지의 누계값", hap)

hap = 0
for x in range(1, 11):
    hap+=x  # hap = hap+x

print("2. 1에서 10까지의 누계값", hap)

# 3. range(start, stop, step)매개변수 3개짜리 함수 이용
# 누적은 하는데 stop값은 포함하지 않는다. 누적을 시킬때 step만큼 건너띄어 리스트를 생성한다.
hap = 0
for x in range(0, 10, 1):
    hap+=x  # hap = hap+x

print("3. 0에서 9까지의 누계값(step 1)", hap)

hap = 0
for x in range(0, 300, 3):
    hap+=x  # hap = hap+x

print("3. 0에서 300까지의 누계값(step 3)", hap)

# range([start], stop, [step])매개변수 3개짜리 함수 이용
# 대괄호에 감싸져 있는 매개변수 값은 생략 가능하다라는 것이다. = 이렇게 되면 1번과 같은 기능을 하게 된다.


# 문자열 실습
# 문자열도 시퀀스의 대상에 포함된다. 하여 for문을 통해서 문자를 추출하여 출력항 수 있다.
s = "jin seung beom"

for ch in s:
    print(ch, end="")
    print(ch, end=" ")