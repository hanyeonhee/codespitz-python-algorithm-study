# Occupied Spaces (주차 공간) CCC '18 J2 - Occupy parking
# https://dmoj.ca/problem/ccc18j2

try:
    # 입력 받기
    n = int(input().strip())
except ValueError:
    print("Error: 입력 값이 정수가 아닙니다.")
    exit()

yesterday = input().strip()
today = input().strip()

# 주차된 공간 수 세기
occupied = 0

for i in range(len(yesterday)):
    if yesterday[i] == "C" and today[i] == "C":
        occupied += 1

# 결과 출력
print(occupied)




