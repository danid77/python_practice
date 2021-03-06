
# 함수를 사용한 프로그램 설계
# 1. 요구사항이 들어오면 철저하게 분석을 해야된다.(요구사항, 명세서, 사규, 데이터 등)
# 2. 문제를 한 번에 해결할려 하지말고 더 작은 크기의 문제들로 분해한다. 문제가 충분히 작아질 떄까지 지속적으로
# 분해를 해야한다.
# 3. 더 이상 분해가 되지 않는 그러한 부분에 고갈 했을 때, 비로소 해당하는 기능을 함수로 만들어서 조립해서 최종적인
# 프로그램을 완성해야 한다.
# 4. 솔루션을 단위테스트 및 통합테스트까지 완료하고, 비로소 회사에 배포하고 안정화 시켜줘야 한다.

# grade.py 모듈을 ex14.py파일을 사용하겠다고 인터프리터에게 알리고 있다.
from grade import *

def main():
    score_list = readList()
    score_list = sortingList(score_list)
    show_score(score_list)

if __name__ == "__main__": #프로그램의 시작점
    main()