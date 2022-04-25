
# 깊은 복사(deep copy) : 주소값을 공유하는 얕은 복사가 아니라 새로운 리스트 객체를 생성헤서 새로운
# 주소값이 할당이 되어 원본 리스트 객체에는 전혀 영향을 끼치지 아니한다.
# 원본과 복사본은 서로 독립적임
# 아래와 같이 3가지 방법으로 만든 리스트가 새로운 객테가 된다.
# 결론적으로 깊은 복사가 진정한 복사가 된다. 

# 첫 번째 방법 : list() 메서드를 이용하는 방법
scores = [10,20,30,40,50]
refer = list(scores)
print("scores의 주소값 : ", id(scores))
print("refer의 주소값 : ", id(refer))

print("두개의 주소값은? : ",scores is refer)
refer[0] = 100
refer.append(-70)
refer.insert(1,-70)

print("scores의 주소값 : ", id(scores))
print("refer의 주소값 : ", id(refer))
print("scores의 값 : ", scores)
print("refer의 값 : ", refer)

print("=========================================================================")

import copy
# 2번째 방법 : COPY모듈에 있는 deepcopy(), copy()를 이용하는 방법
print("deepcopy")
scores_copy = [10,20,30,40,50]
refer_copy = copy.deepcopy(scores_copy)
print("scores의 주소값 : ", id(scores_copy))
print("refer의 주소값 : ", id(refer_copy))

print("두개의 주소값은? : ",scores_copy is refer_copy)
refer_copy[0] = 100
refer_copy.append(-70)
refer_copy.insert(1,-70)

print("scores의 주소값 : ", id(scores_copy))
print("refer의 주소값 : ", id(refer_copy))
print("scores의 값 : ", scores_copy)
print("refer의 값 : ", refer_copy)

print("=========================================================================")
print("copy")
scores_copy = [10,20,30,40,50]
refer_copy = copy.copy(scores_copy)
print("scores의 주소값 : ", id(scores_copy))
print("refer의 주소값 : ", id(refer_copy))

print("두개의 주소값은? : ",scores_copy is refer_copy)
refer_copy[0] = 100
refer_copy.append(-70)
refer_copy.insert(1,-70)

print("scores의 주소값 : ", id(scores_copy))
print("refer의 주소값 : ", id(refer_copy))
print("scores의 값 : ", scores_copy)
print("refer의 값 : ", refer_copy)

print("=========================================================================")

# 3번쨰 방법 : [:] 인덱스를 이용하여 깊은 복사를 하는 방법
scores_index = [10,20,30,40,50]
refer_index = scores_index[:]
print("scores의 주소값 : ", id(scores_index))
print("refer의 주소값 : ", id(refer_index))

print("두개의 주소값은? : ",scores_index is refer_index)
refer_index[0] = 100
refer_index.append(-70)
refer_index.insert(1,-70)

print("scores의 주소값 : ", id(scores_index))
print("refer의 주소값 : ", id(refer_index))
print("scores의 값 : ", scores_index)
print("refer의 값 : ", refer_index)

print("=========================================================================")