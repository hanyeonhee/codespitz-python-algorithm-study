# ECOO '12 R1 P2 - DNA 디코딩
# https://dmoj.ca/problem/ecoo12r1p2

def find_promoter(dna):
    # TATAAT 서열을 찾아 그 위치를 반환합니다.
    # 찾지 못하면 -1을 반환합니다.
    return dna.find('TATAAT')


def find_terminator(dna, start):
    # 종결 코돈을 찾는 함수입니다.
    for i in range(start, len(dna) - 5):
        seq = dna[i:i + 6]  # 6개의 염기를 선택합니다.
        # 선택한 서열의 역상보서열을 만듭니다.
        rev_comp = ''.join(['TAGC'['ATCG'.index(base)] for base in seq[::-1]])
        # 역상보서열이 이후 DNA에 존재하는지 확인합니다.
        if rev_comp in dna[i + 6:]:
            return i  # 종결 코돈의 시작 위치를 반환합니다.
    return len(dna)  # 종결 코돈을 찾지 못하면 DNA의 끝을 반환합니다.


def transcribe(dna):
    # DNA를 RNA로 전사합니다. T를 U로 바꿉니다.
    return dna.replace('T', 'U')


def complement(rna):
    # RNA의 상보적 서열을 만듭니다.
    return ''.join(['UAGC'['AUCG'.index(base)] for base in rna])


def process_dna(dna):
    # 프로모터 위치를 찾습니다.
    promoter_index = find_promoter(dna)
    if promoter_index == -1:
        return ''  # 프로모터가 없으면 빈 문자열을 반환합니다.

    # 전사 시작 위치 (프로모터 + 10)
    start = promoter_index + 10
    # 종결 코돈 위치
    end = find_terminator(dna, start)

    if start >= end:
        return ''  # 유효한 전사 단위가 없으면 빈 문자열을 반환합니다.

    # 전사 단위를 추출합니다.
    transcription_unit = dna[start:end]
    # DNA를 RNA로 전사합니다.
    rna = transcribe(transcription_unit)
    # RNA의 상보적 서열을 반환합니다.
    return complement(rna)


# 입력 처리 및 결과 출력
for i in range(5):
    try:
        # 사용자로부터 DNA 서열을 입력받습니다.
        dna = input().strip()
        # DNA를 처리하고 결과를 얻습니다.
        result = process_dna(dna)
        # 결과를 출력합니다.
        print(f"{i + 1}: {result}")
    except EOFError:
        # 입력이 끝나면 루프를 종료합니다.
        break