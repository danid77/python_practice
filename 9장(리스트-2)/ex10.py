
# 정렬하기 실습
list1 = [4,8,9,-1,10]

# 리스트객체에서 재공해주는 sort()를 이용하여 정렬하는 방법
list1.sort()
print(list1)
list1.sort(reverse=True)
print(list1)

# 선택정렬 알고리즘을 통한 정렬하기
# 선택 정렬이라는 주어진 리스트 중에서 최소값을 찾는다.
# 그 최소값을 맨 앞에 위치한 값과 교환한다.
# 맨 처음위치를 뺀 나머지 리스트를 위와 똑같은 방법으로 루핑하면서 최종적으로 정렬이 이루어진다.
# 선택정렬은 제자리; 정렬이기 때문에 더블루프를 사용해야 한다.
# li[min_idx] > li[j]의 부등호를 바꾸면 내림차순이됨
def selectSort(li):
    cnt = 0
    for i in range(len(li) - 1):
        min_idx = i
        for j in range(i+1, len(li)):
            if li[min_idx] > li[j]:
                min_idx = j
                cnt += 1

        if min_idx != i:     # 최소값을 찾았다면...
            # 두 인덱스의 해당하는 값을 서로 바꾸고 있다.
            print(li[min_idx], li[i], "을 교환합니다. ")
            li[i], li[min_idx] = li[min_idx], li[i]
    print(cnt, "만큼 교환이 이루어졌습니다. ")
    return li

# 버블정렬 알고리즘
# 인접한 두 원소를 검사하는 방법인데 정확도는 높다.
# 데이터가 많아지면 질수록 속도가 떨어진다.
# li[j] > li[j+1]의 부등호를 바꾸면 내림차순됨
def bubble_sort(li):
    list_length = len(li)               # 길이가 10
    for i in range(list_length-1):
        for j in range(list_length-i-1):    # -1을 하는 이유는 i가 0일때 인덱스 오류가 발생한다.
            if li[j] > li[j+1]:
                li[j], li[j+1] = li[j+1], li[j]
        print(i,j,j+1,li)



if __name__ == "__main__":
    # 하나를 기준으로 다른 요소들을 루프를 돌면서 비교하는 방식이 선택정렬이다.
    li = [4,5,6,7,8,10,-50,-33,-56,100]
    selectSort(li)
    print(li)
    print("=========================================================")
    li = [4, 1, -56, 100]
    bubble_sort(li)
    print(li)