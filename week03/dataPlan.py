# Data Plan (데이터 요금제) COCI '16 Contest 1 #1 Tarifa
# https://dmoj.ca/problem/coci16c1p1

try:
    # 첫 줄에서 X 값 입력 받기
    X = int(input().strip())
except ValueError:
    print("Error: 입력 값이 정수가 아닙니다.")
    exit()

try:
    # 두 번째 줄에서 N 값 입력 받기
    N = int(input().strip())
except ValueError:
    print("Error: 입력 값이 정수가 아닙니다.")
    exit()

# 사용된 데이터 양 입력 받기
used_data = []
for _ in range(N):
    try:
        used_data.append(int(input().strip()))
    except ValueError:
        print("Error: 입력 값이 정수가 아닙니다.")
        exit()

# 총 사용된 데이터 양 계산
total_used = sum(used_data)

# N+1 번째 달에 사용할 수 있는 총 데이터 양 계산
total_available = (N + 1) * X - total_used

# 결과 출력
print(total_available)
