# COCI '12 Contest 5 #1 Ljestvica
# https://dmoj.ca/problem/coci12c5p1
def determine_scale(composition):
    # C-major와 A-minor의 주요 음
    c_major = set(['C', 'F', 'G'])
    a_minor = set(['A', 'D', 'E'])

    # 마디의 첫 음을 추출
    accented_tones = [measure[0] for measure in composition.split('|')]

    # C-major와 A-minor의 주요 음 개수 세기
    c_major_count = sum(1 for tone in accented_tones if tone in c_major)
    a_minor_count = sum(1 for tone in accented_tones if tone in a_minor)

    # 개수가 같으면 마지막 음을 확인
    if c_major_count == a_minor_count:
        return "C-dur" if composition[-1] == 'C' else "A-mol"

    # 개수가 다르면 더 많은 쪽을 선택
    return "C-dur" if c_major_count > a_minor_count else "A-mol"

# 입력 받기
composition = input().strip()

# 결과 출력
result = determine_scale(composition)
print(result)