# Three cups (야바위), COCI '06 Contest 5 #1 Trik
# https://dmoj.ca/problem/coci06c5p1

# 초기 위치 설정 (공은 처음에 왼쪽 컵에 있음)
위치 = 1

# 입력된 움직임 문자열 읽기
움직임 = input().strip()

# 각 움직임에 대해 위치 갱신
for 움직임 in 움직임:
    if 움직임 == 'A':
        if 위치 == 1:
            위치 = 2
        elif 위치 == 2:
            위치 = 1
    if 움직임 == 'B':
        if 위치 == 2:
            위치 = 3
        elif 위치 == 3:
            위치 = 2
    if 움직임 == 'C':
        if 위치 == 1:
            위치 = 3
        elif 위치 == 3:
            위치 = 1

# 최종 위치 출력
print(위치)
