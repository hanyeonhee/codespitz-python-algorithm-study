# COCI '18 Contest 4 #1 Elder
# https://dmoj.ca/problem/coci18c4p1

def elder_wand_simulation(initial_wizard, duels):
    current_wizard = initial_wizard
    obeyed_wizards = set([current_wizard])

    for winner, loser in duels:
        if loser == current_wizard:
            current_wizard = winner
            obeyed_wizards.add(current_wizard)

    return current_wizard, len(obeyed_wizards)


# 입력 받기
initial_wizard = input().strip()
N = int(input())
duels = [input().split() for _ in range(N)]

# 시뮬레이션 실행
final_wizard, different_wizards = elder_wand_simulation(initial_wizard, duels)

# 결과 출력
print(final_wizard)
print(different_wizards)