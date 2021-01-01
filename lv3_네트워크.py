from collections import deque
def solution(n, computers):
    answer = 0
    visited = [False] * n
    q = deque()

    for j in range(n):
        if visited[j] == True:
            continue
        q.append(j)
        while q:
            node = q.popleft()
            visited[node] = True

            for i in range(n):
                if visited[i] == False and computers[node][i] == 1:
                    q.append(i)
        answer += 1

    return answer


# union & find로 풀기
