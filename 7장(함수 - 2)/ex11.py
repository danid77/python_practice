
# 여러개의 값을 반환하는 함수 실습
# 타 프로그래밍 언어에서는 함수는 항상 하나의 값만을 반환하거나 반환값이 없다는 것이 원척이다.
# 하지만 파이썬은 튜플을 이용해서 여러개의 값을 반환 할 수 있다.
# 튜플은 몇가지를 제외하고 리스트와 거의 비슷한 자료구조 형태이다.
# - 리스트 [], 튜플() 로 값을 감싼다.
# - 리스트는 변경(생성, 추가, 수정, 삭제)가능한 객체, 튜블은 한번 값을 만들면 그 값을 변경할 수 없다.

# 파이썬에서는 튜플의 형태로 여러개의 값을 리턴하지만, 함수에서 하나의 값만 리턴할 수 잇다는 정설에 부합하다.
# 그이유는 튜플이라는 자료형 때문에 1개의 값으로 인식한다. 
def tuple_return():
    return 1,"안녕",5

a,b,c = tuple_return()
tuple_variable = tuple_return()
# tuple_variable += 10   튜플은 수정이 불가능 - 값을 추가 못함

print(a,b,c)
print(tuple_variable)
print(type(tuple_variable))

li = list(tuple_variable)
li += "반갑습니다."
li.append("안녕히가세요.")
print(li)