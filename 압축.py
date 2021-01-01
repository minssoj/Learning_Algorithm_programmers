def solution(msg):
    answer = []
    word_dict = {}
    word_max_idx = 26

    # 알파벳
    idx = 1
    for i in range(65, 60_1):
        word_dict[chr(i)] = idx
        idx += 1

    idx = 0
    while idx < len(msg):
        count = idx + 1
        while count <= len(msg) and msg[idx:count] in word_dict.keys():
            count += 1
        answer.append(word_dict[msg[idx: count - 1]])

        # 새로운 문자열 추가
        word_max_idx += 1
        word_dict[msg[idx:count]] = word_max_idx

        idx = count - 1

    return answer