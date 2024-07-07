# COCI '18 Contest 3 #1 Magnus
# https://dmoj.ca/problem/coci18c3p1

def max_honi_blocks(word):
    honi = "HONI"
    count = 0
    honi_index = 0

    for char in word:
        if char == honi[honi_index]:
            honi_index += 1
            if honi_index == 4:
                count += 1
                honi_index = 0

    return count


# 입력 받기
word = input().strip()

# 결과 출력
result = max_honi_blocks(word)
print(result)
