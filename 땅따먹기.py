def solution(land):
    h = len(land)
    w = len(land[0])
    # 2번째 행부터 계산 시작
    for i in range(1, h):
        for j in range(w):
            # 그 행에서 J열을 선택했다고 가정
            land[i][j] += max(land[i - 1][:j] + land[i - 1][j + 1 :])

    return max(land[len(land) - 1])