def solution(n):
    answer = 0
    for i in range(1, n//2 + 1):
        sum_ = 0
        sum_ += i
        for j in range(i+1, n // 2 + 2):
            sum_ +=j
            if sum_ == n:
                answer += 1
                break
            elif sum_ > n:      # 넘으면 더 돌지 않도록 ! 시간 초과의 원인
                break
    return answer+1