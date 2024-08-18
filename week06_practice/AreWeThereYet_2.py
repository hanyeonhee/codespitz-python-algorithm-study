# CCC '18 J3 - Are we there yet? (도시 간 거리 계산하기)
# https://dmoj.ca/problem/ccc18j3

# 입력 받기
distances = list(map(int, input().split()))

# 도시의 총 개수 (입력된 거리의 수 + 1)
num_cities = len(distances) + 1

# 결과를 저장할 2차원 리스트 초기화
result = [[0] * num_cities for _ in range(num_cities)]

# 각 도시 쌍에 대한 거리 계산
for i in range(num_cities):
    for j in range(num_cities):
        if i == j:
            continue  # 같은 도시 간의 거리는 0
        elif i < j:
            # i부터 j까지의 거리 합산
            result[i][j] = sum(distances[i:j])
        else:
            # j부터 i까지의 거리 합산
            result[i][j] = sum(distances[j:i])

# 결과 출력
for row in result:
    print(' '.join(map(str, row)))