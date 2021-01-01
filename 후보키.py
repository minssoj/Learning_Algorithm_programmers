from itertools import combinations


def solution(relation):
    n_row = len(relation)
    n_col = len(relation[0])

    # 부분집합을 모두 구함
    candidates = []
    for i in range(1, n_col + 1):
        candidates.extend(combinations(range(n_col), i))

    # print(candidates)
    # [(0,), (1,), (2,), (3,), (0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3),
    # (0, 1, 2), (0, 1, 3), (0, 2, 3), (1, 2, 3), (0, 1, 2, 3)]

    # 부분집합을 만들어서 유일한지 판단
    final = []
    for keys in candidates:
        tmp = [tuple([item[key] for key in keys]) for item in relation]
        # 중복제거해서 남은게 원래 row개수와 같다면 통과
        if len(set(tmp)) == n_row:
            final.append(keys)

    answer = set(final[:])  # 집합으로 형변환
    # answer : {(0, 1), (1, 2), (0,), (0, 1, 2), (0, 2, 3), (0, 1, 3),
    # (1, 2, 3), (0, 3), (0, 2), (0, 1, 2, 3)}

    # final : [(0,), (0, 1), (0, 2), (0, 3), (1, 2), (0, 1, 2), (0, 1, 3),
    # (0, 2, 3), (1, 2, 3), (0, 1, 2, 3)]

    # 최소성 판단
    for i in range(len(final)):
        for j in range(i + 1, len(final)):
            if len(final[i]) == len(set(final[i]).intersection(set(final[j]))):
                answer.discard(final[j])

    return len(answer)