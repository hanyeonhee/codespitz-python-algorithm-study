# 페인트의 총량
paint = int(input())

# 배지 하나를 만드는 데 필요한 페인트의 양
badge = int(input())

# 배지 하나의 가격
price = int(input())

# 배지의 최대 개수를 계산
max_badges = paint // badge

# 배지를 만든 후 남는 페인트의 양을 계산
remaining_paint = paint % badge

# 배지를 팔아서 얻는 수입을 계산
income_from_badges = max_badges * price

# 남은 페인트를 팔아서 얻는 수입을 계산
income_from_paint = remaining_paint

# 총 수입을 계산
total_income = income_from_badges + income_from_paint

# 총 수입을 출력
print(total_income)