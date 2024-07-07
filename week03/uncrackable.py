# WC '17 Contest 3 J3 - Uncrackable
# https://dmoj.ca/problem/wc17c3j3

def is_valid_password(password):
    if not 8 <= len(password) <= 12:
        return False

    lowercase_count = 0
    uppercase_count = 0
    digit_count = 0

    for char in password:
        if char.islower():
            lowercase_count += 1
        elif char.isupper():
            uppercase_count += 1
        elif char.isdigit():
            digit_count += 1
        else:
            return False  # 허용되지 않는 문자가 있으면 무효

    return (lowercase_count >= 3 and
            uppercase_count >= 2 and
            digit_count >= 1)


# 입력 받기
password = input().strip()

# 결과 출력
if is_valid_password(password):
    print("Valid")
else:
    print("Invalid")
