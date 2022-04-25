
# 기본적인 파일 입출력 실습

data = []
# 파일의 경로를 지정하고 읽기 모드로 문자 셋 UTF-8로 설정해서 해당 파일을 열고
# 메모리에 로딩된 파일의 주소를 반환한다.
fp = open("C:\\Temp\\qna개시판 답변.txt", mode="r", encoding="UTF-8")
# print(type(fp))
# readlines()메서드는 파일의 저장된 내용을 한번에 다 읽는다.
for line in fp.readlines():
    # strip()메서드는 원래 문자열의 양쪽 공백을 제거하는 역할을 하지만,
    # 파일을 읽어들일때는 엔터키 제거를 해준다.
    data.append(line.strip())

print("파일에서 읽은 내용입니다.")
print(data)

# 프로그램에서 리소스를 다 사용 했으면 반드시 close()메소드를 호출해야 한다. 
fp.close()

print("=========================================================")
# 파일에 내용을 쓰는 방법
# 파일의 모드가 w인 경우에는 기존파일의 내용을 덮어써버린다.
fp = open("C:\\Temp\\qna개시판 답변.txt", mode="w", encoding="UTF-8")
fp.write("우리는 파이썬을 공부합니다.")
fp.write("저희도 파이썬을 공부합니다.")

fp.close()

print("=========================================================")
# 파일에 내용을 쓰는 방법
# 파일의 모드가 a인 경우에는 기존파일의 내용에 추가한다.
fp = open("C:\\Temp\\qna개시판 답변.txt", mode="a", encoding="UTF-8")
fp.write("우리는 파이썬을 공부합니다.")
fp.write("저희도 파이썬을 공부합니다.")
print("추가 완료")

fp.close()