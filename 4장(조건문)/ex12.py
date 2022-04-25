
# 논리 연산자(logical operator)는 두개 이상의 도건을 조합해서 참인지
# 거진인지를 계산할때 사용하는 연산자이다.
# 논리연산자의 종류
# and(논리곱)
# or(논리합)
# not(논리 부정)

# and 논리 연산자의 실습
# 조건중 하나라도 거짓이면 거짓
name = "신은혁"
age = 13
height  = 160

# and논리 연산자는 여러개의 조건 중에서 처음 조건이 거짓이라면 다른 조건은 전혀 검사조차도 하지 않는다.(단축 계산)
if(age >= 14) and (height>= 160) and (name == "신은혁") :
    print(name + "님은 놀이 기구를 탈 수 있습니다.")
else:
    print(name + "님은 놀이 기구를 탈 수 없습니다. ")

print("------------------------------------")

# or연산자
# 조건중 하나라도 참이면 참
# 조건중 모든 조건아 거짓일때 거짓
name = "신은혁"
age = 13
height  = 160

if(age >= 14) or (height>= 160) or (name == "신은혁") :
    print(name + "님은 놀이 기구를 탈 수 있습니다.")
else:
    print(name + "님은 놀이 기구를 탈 수 없습니다. ")

print("------------------------------------")

# not
# 조건식의 값을 반대로 바꿈(참 ->거짓, 거짓 -> 참)
if not(1==0):
    print("ture")

if not(1==1):
    print("ture")
else:
    print("false")