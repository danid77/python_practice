
# 학생들의 성적을 처리하는 프로그램을 만들기
# 조건 : 사용자로부터 성적을 입력 받아서 리스트에 저장한다.
# 성적의 평균을 구하고 해당 점수가 80이상 성적을 받은 학생의 수를 출력하세요.
# 출력결과

# 성적의 합계와 평균을 구해주는 함수

def sum(a):
    hap = 0
    for i in range(len(a)):
        hap = hap + a[i]

    print("성적의 합은 : ", hap)
    avg = round(float(hap/len(a)),2)
    print("성적의 평균은 : ",avg)


scores = []
scores_80 = []
for i in range(5):
    scores.append(int(input("성적을 입력하세요 : ")))
    if scores[i] >= 80 :
        scores_80.append(scores[i])


print(scores)

sum(scores)
print(scores_80)
print("80이 넘는 학생은 : ", len(scores_80))

print("================================================")
print("선생님 풀이")
# 학생수는 상수값으로 student = 5를 이용한다.

STUDENT = 5         # 전역상수 선언
scores_1  =  []     # 학생들의 성적을 저장할 리스트
scores_Sum = 0      # 학생들의 성적 합계를 저장할 변수
scores_Avg = 0.0      # 학생들의 성적 평균을 저장할 변수
cnt_80 = 0            # 80점 이상인 학생 수 합계를 저장할 변수

for i in range(5):
    score = int(input("성적을 입력하세요 : "))
    scores_1.append(score)          # 학생들의 성적을 lit에 저장함
    scores_Sum += score             # 합계
    if score >= 80:                 # 80점 이상 명수
        cnt_80 += 1

scores_Avg = scores_Sum / len(scores_1) #평균
print("학생 평균은 ", scores_Avg,"입니다.")