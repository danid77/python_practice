# 모듈을 활용하는 첫 번째 방법
import fibo

# fibo 모듈의 fib()를 사용하겠다라는 것이다.
fibo.fib(1000)
print("")
print("------------------------------")
fibo.fib(10000)

print("")
print("------------------------------")

# fibo 모듈의 sum()를 사용하겠다라는 것이다.
print(fibo.sum(10))
print(fibo.sum(100))

print("=========================================================")

# 모듈을 활용하는 두 번째 방법
from fibo import *

fib(1000)
print("")
print(sum(10))

# 위 두개의 차이점은 import를 사용하면 파일명, 함수명()으로 호출되므로 사용한 함수의 출처를 알 수가 있다.
# from fibo import *를 사용하면 파일명 필요가 없다.
# 함수명으로 바로 호출이 가능하다.

# __name__은 내장 전역변수로 인터프리터가 만들어 놓은 것이다.
print(fibo.__name__)

# 실행파일에서는 __name__ 라는 내장전역변수는 __main__ 값을 가지게 된다.
print(__name__)


def main():
    # fibo 모듈의 fib()를 사용하겠다라는 것이다.
    fibo.fib(1000)
    # fibo 모듈의 sum()를 사용하겠다라는 것이다.
    print(fibo.sum(10))
    print(fibo.__name__)
    print(__name__)


if __name__ == "__main__":  # 프로그램의 시작점이 되는 형태
# # fibo 모듈의 fib()를 사용하겠다라는 것이다.
# fibo.fib(1000)
# # fibo 모듈의 sum()를 사용하겠다라는 것이다.
# print(fibo.sum(10))
# print(fibo.__name__)
# print(__name__)
    main()
