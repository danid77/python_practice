
# 함수를 만들어서 큐 실습하기

# 큐에 저장하는 함수
def offer(data, n):     # data : 스택 리스트(장소), n : 추가할 값
    data.append(n)

# 큐에서 삭제하는 함수
def poll(data):
    if len(data) > 0:
        return data.pop(0)
    return False

# 큐에
def offer_insert(data):
    for i in range(1,5):
        offer(data, i)
        print("큐의 현제 상태 : ", data)

def offer_delete(data):
    for i in range(1, 5):
        poll(data)
        print("큐의 현제 상태 : ", data)


if __name__ == "__main__":
    queue = []
    offer_insert(queue)
    offer_delete(queue)