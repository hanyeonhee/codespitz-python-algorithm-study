# Three cups (야바위), COCI '06 Contest 5 #1 Trik
# https://dmoj.ca/problem/coci06c5p1

moves = input()  # 사용자로부터 움직임 입력을 받음

# 입력된 문자열에 A, B, C 외의 문자가 있으면 프로그램을 종료
if moves.count("A") + moves.count("B") + moves.count("C") != len(moves):
    exit("문자열에 A, B, C 이외의 문자가 있음")

cups = "123"  # 컵의 초기 위치를 나타내는 문자열
for move in moves:  # 입력된 움직임을 하나씩 처리
    if move == "A":  # A 움직임: 첫 번째와 두 번째 컵의 위치를 교환
        cups = cups[1] + cups[0] + cups[2]
    elif move == "B":  # B 움직임: 두 번째와 세 번째 컵의 위치를 교환
        cups = cups[0] + cups[2] + cups[1]
    else:  # move == "C":  # C 움직임: 첫 번째와 세 번째 컵의 위치를 교환
        cups = cups[2] + cups[1] + cups[0]

# 공이 있는 컵의 위치를 출력 (컵의 위치는 1부터 시작하므로 1을 더함)
print(cups.find("1") + 1)

