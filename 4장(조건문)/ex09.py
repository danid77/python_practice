
# 블록의 중요성에 대한 실습
# 타 언어(java, c, c++ 등)에서는 블록을 중괄호를 감싸ㅛㅓ 들여쓰기를 해야한다라는 문법이 없다.

# 자바
# if(10>5) {
#     print("참입니다.");
# }else {
#     print("거짓입니다.");
# }

# 파이썬에서는 블록을 만들 때, 반드시 공간을 동일하게 줘야 한다.
# 파이썬의 문법에서는 블록(실행문장이 여러개일 때)을 만들 때, 반드시 들여쓰기를 해야 한다.
score = 95
if score >= 95:
      # print("합격입니다. ")  IndentationError: unindent does not match any outer indentation level
      # 들여쓰기 오류
    print("합격입니다. ")
    print("장학금도 받을 수 있습니다. ")