# 정수를 입력 받아서 시, 분, 초로 변경하는 프로그램

time = int(input("초를 입력하세요 : "))

# 60으로 나눈 나머지는 초를 의미
second = time % 60
# 60으로 나눈 몫을 다시 60으로 나눈 나머자는 분을 의미
minute = (time/60)%60
# 60으로 나눈 몫을 다시 60으로 나눈 몫은 시간을 의미
hour = (time/60)/60

print("시간 : ", hour, "분 : ",  minute, "초 : ", second)