# CCC '13 S1 - From 1987 to 2013
# https://dmoj.ca/problem/ccc13s1
def is_distinct(year):
    return len(set(str(year))) == len(str(year))

def next_distinct_year(year):
    year += 1
    while not is_distinct(year):
        year += 1
    return year

# 입력 받기
start_year = int(input())

# 다음 고유 숫자 연도 찾기
result = next_distinct_year(start_year)

# 결과 출력
print(result)