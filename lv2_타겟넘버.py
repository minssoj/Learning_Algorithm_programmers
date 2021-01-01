def solution(numbers, target):
    answer = 0
    def dfs(i, tot):
        if i == len(numbers):
            if tot == target:
                nonlocal answer
                answer += 1
        else:
            dfs(i+1, tot + numbers[i])
            dfs(i+1, tot - numbers[i])
    dfs(0,0)
    return answer