#COCI '07 Regional #1 Platforme
#https://dmoj.ca/problem/crci07p1

# 플랫폼의 수를 입력받습니다
N = int(input())

# 플랫폼 정보를 저장할 리스트를 초기화합니다
platforms = []

# N개의 플랫폼 정보를 입력받아 리스트에 저장합니다
for _ in range(N):
    y, x1, x2 = map(int, input().split())
    platforms.append((y, x1, x2))

# 플랫폼을 y 좌표(높이)를 기준으로 내림차순 정렬합니다
platforms.sort(reverse=True)

# 총 기둥 길이를 저장할 변수를 초기화합니다
total_length = 0

# 각 플랫폼에 대해 처리합니다
for i, (y, x1, x2) in enumerate(platforms):
    # 왼쪽 기둥의 길이를 계산합니다
    left_pillar = y
    # 오른쪽 기둥의 길이를 계산합니다
    right_pillar = y

    # 현재 플랫폼 아래에 있는 모든 플랫폼을 확인합니다
    for lower_y, lower_x1, lower_x2 in platforms[i + 1:]:
        # 왼쪽 기둥이 아직 최대 길이라면
        if left_pillar == y:
            # 아래 플랫폼이 왼쪽 기둥을 지지할 수 있는지 확인합니다
            if lower_x1 <= x1 < lower_x2:
                left_pillar = y - lower_y

        # 오른쪽 기둥이 아직 최대 길이라면
        if right_pillar == y:
            # 아래 플랫폼이 오른쪽 기둥을 지지할 수 있는지 확인합니다
            if lower_x1 < x2 <= lower_x2:
                right_pillar = y - lower_y

        # 양쪽 기둥의 길이가 모두 결정되었다면 더 이상 확인할 필요가 없습니다
        if left_pillar < y and right_pillar < y:
            break

    # 이 플랫폼의 양쪽 기둥 길이를 총 길이에 더합니다
    total_length += left_pillar + right_pillar

# 총 기둥 길이를 출력합니다
print(total_length)