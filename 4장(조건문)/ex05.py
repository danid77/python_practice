

# 사용자에게 명렬어를 입력받아서 터틀그래픽을 제어를 해보자. 즉
# 사용자가 "left"를 압력 하면 횐쪽으로 회전하게 되고 사용자가 "right"를 입력했다면 오른쪽으로 회전하게 하는
# 프로그램 만들기

import turtle
# 팬의 기능을 t변수에 저장
t = turtle.Pen()

# 반복문을 무한 루프를 돌려 if 구문을 이용하여 방향을 제어하는 코드
# 무한루프를 프로그래밍을 했다면 반드시 루프를 탈출하는 코드가 반드시 있어야 된다.(중요)

while True:
    direction = input("왼쪽 = left, 오른쪽 = right, 종료 = quit 입력 : ")

    # break는 반복문을 빠져나가는 코드
    if direction == "quit":
        break

    # 사용자가 left를 입력했을때
    if direction == "left":
        print("왼쪽으로 60 만큼 이동")
        t.left(60)
        t.forward(60)

    # 사용자가 갸홋를 입력했을때
    if direction == "right":
        print("오른쪽으로 60 만큼 이동")
        t.right(60)
        t.forward(60)

# 터틀 그래픽 창이 클릭을 해야 사라지게 하는 코드
turtle.exitonclick()