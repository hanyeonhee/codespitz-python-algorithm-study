# COCI '13 Contest 2 #2 Misa
# https://dmoj.ca/problem/coci13c2p2

# 입력 받기
R, S = map(int, input().split())
church = [list(input().strip()) for _ in range(R)]

# 8방향 이동을 위한 델타 값 정의
dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]

def count_handshakes(x, y):
    """주어진 좌표에서 가능한 악수 횟수를 계산합니다."""
    count = 0
    for i in range(8):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < R and 0 <= ny < S and church[nx][ny] == 'o':
            count += 1
    return count

# 현재 교회 상태에서의 악수 횟수 계산
total_handshakes = 0
for i in range(R):
    for j in range(S):
        if church[i][j] == 'o':
            total_handshakes += count_handshakes(i, j)

# Mirko가 앉을 수 있는 최적의 위치 찾기
max_additional_handshakes = 0
for i in range(R):
    for j in range(S):
        if church[i][j] == '.':
            additional_handshakes = count_handshakes(i, j)
            max_additional_handshakes = max(max_additional_handshakes, additional_handshakes)

# 전체 악수 횟수 계산 (기존 악수 + Mirko의 추가 악수)
total_handshakes = total_handshakes // 2 + max_additional_handshakes

print(total_handshakes)