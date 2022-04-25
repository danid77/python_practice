# defaultdict 의 초깃값을 리스트 형태로 만드는 실습

from collections import defaultdict

#          튜플 값
li1 = [("yellow",1),("blue",2),("green",3),("blue",4),("red",1)]
dic1 = defaultdict(list)

# for문 에서 li1을 k,v변수에 담아 사용하겠다.
for k, v in li1:
    dic1[k].append(v)

print(dic1.items())
print(dic1)
