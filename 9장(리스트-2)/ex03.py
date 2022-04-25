
# 값으로 호출, 참조로 호출의 차이점

def func(x):
    print("x = ", x, "address = ", id(x))
    x += 15
    print("x = ", x, "address = ", id(x))
    
y = 10      # 정수형 (변경이 불가능한 객체)
print("y = ", y, "address = ", id(y))
func(y)     # 함수 호출(값에 의한 호출)
print("y = ", y, "address = ", id(y))

print("===========================================")

def func(x):
    print("x = ", x, "address = ", id(x))
    x += "하세요"
    print("x = ", x, "address = ", id(x))

y = "안녕"      # 문자열 (변경이 불가능한 객체)
print("y = ", y, "address = ", id(y))
func(y)     # 함수 호출(값에 의한 호출)
print("y = ", y, "address = ", id(y))

print("===========================================")
# 주소값이 모두 같다. 왜냐하면 주소값만 전달하기 때문에 하나의 객체를 공유하고 있다. 
def func_list(x):
    print("x = ", x, "address = ", id(x))
    x += "하세요"
    print("x = ", x, "address = ", id(x))

y = [10,20,30]  # 리스트형(변경 가능한 객체)
print("y = ", y, "address = ", id(y))
func(y)     # 함수 호출(값에 의한 호출)
print("y = ", y, "address = ", id(y))