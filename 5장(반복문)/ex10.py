import turtle
from turtle import *
# 터틀 그래픽을 활용해서 for문으로 별 모양을 그려보는 프로그램

t = turtle.Pen()

for i in range(5):
    t.forward(200)
    t.right(144)

turtle.exitonclick()