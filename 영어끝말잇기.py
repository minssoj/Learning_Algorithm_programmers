def solution(n, words):
    answer = [0, 0]
    word_list = []
    for idx, word in enumerate(words):
        if idx > 0 and words[idx][0] != words[idx - 1][-1]:
            answer[1] = idx // n + 1
            answer[0] = idx % n + 1
            return answer
        if word in word_list:
            answer[1] = idx // n + 1
            answer[0] = idx % n + 1
            return answer
        else:
            word_list.append(word)

    return answer
