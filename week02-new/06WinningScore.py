# 두 팀의 점수를 비교하여 누가 이겼는지 결정하기
# 팀의 3점 슛, 2점 필드골, 1점 프리스로의 수를 입력 받아 점수를 계산하기

def winning_score():
    # 첫 번째 팀의 점수 입력 받기
    apples_3pt = int(input())
    apples_2pt = int(input())
    apples_1pt = int(input())

    # 두 번째 팀의 점수 입력 받기
    bananas_3pt = int(input())
    bananas_2pt = int(input())
    bananas_1pt = int(input())

    # 각 팀의 총 점수 계산하기
    apples_score = apples_3pt * 3 + apples_2pt * 2 + apples_1pt
    bananas_score = bananas_3pt * 3 + bananas_2pt * 2 + bananas_1pt

    # 결과 출력하기
    if apples_score > bananas_score:
        print("A")
    elif apples_score < bananas_score:
        print("B")
    else:
        print("T")

winning_score()
