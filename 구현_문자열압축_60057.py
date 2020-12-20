# 문제 : https://programmers.co.kr/learn/courses/30/lessons/60057
def solution(s):
    answer = len(s)
    for l in range(len(s)//2, 0, -1):
        after = ''
        pattern = s[0:l]
        count = 1
        for p in range(l, len(s), l):
            if pattern == s[p:p+l]:
                count += 1
            else:
                after += str(count) + pattern if count>1 else pattern
                pattern = s[p:p+l]
                count = 1
        after += str(count) + pattern if count>1 else pattern
        answer = min(answer, len(after))
    return answer
