import turtle
from turtle import *
# 터틀 그래픽을 이용해서 사각형 3개를 그려보자
# ,단 조건은 사각형을 20도씩 기울어져 있다.

t = turtle.Pen()

for i in range(10):
    t.left(20)  #왼쪽으로 20도 회전

#     아래는 사각형을 만드는 코드이다.
    for j in range(4):
        t.forward(100)
        t.left(90)
    # t.forward(100)
    # t.left(90)
    # t.forward(100)
    # t.left(90)
    # t.forward(100)
    # t.left(90)
    # t.forward(100)
    # t.left(90)


turtle.exitonclick()