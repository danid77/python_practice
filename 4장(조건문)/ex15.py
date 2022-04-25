
# if ~ elif ~ else(옵션) 대한 실습

score = int(input("성적을 입력하세요(0~100)"))

# 다중조건중 하나만 만족하면 그 이후 조건은 검사하지 않는다.(중요)
if score >= 90:
    print("학점 A")
elif score >= 80:
    print("학점 B")
elif score >= 70:
    print("학점 C")
elif score >= 60:
    print("학점 D")
else : # else구문은 조건식이 붙을 수 없다. 
    print("학점 F")