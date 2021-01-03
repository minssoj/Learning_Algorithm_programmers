# time을 증가시키면서, 완료된 일 빼기
# 같은 시간에 완료된 일 갯수 카운트하여 정답에 append하기
# 단, 카운트가 0인 경우는 append하지 않는다.
from collections import deque
def solution(progresses, speeds):
    progresses_ = deque(progresses)
    speeds_ = deque(speeds)
    answer = []
    time = 0
    count = 0
    while progresses_:
        if (progresses_[0]+ time*speeds_[0]) >= 100:
            progresses_.popleft()
            speeds_.popleft()
            count += 1
        else:
            if count > 0:
                answer.append(count)
                count = 0
            time += 1
    answer.append(count)
    return answer