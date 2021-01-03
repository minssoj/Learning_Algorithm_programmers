def solution(n, results):
    answer = 0

    # graph[m][n] : m이 n을 이기면 True
    graph = [[False] * (n + 1) for _ in range(n + 1)]

    for r in results:
        graph[r[0]][r[1]] = True

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            for k in range(1, n + 1):
                if graph[j][i] and graph[i][k]:
                    graph[j][k] = True

    for i in range(1, n + 1):
        count_ = 0
        for j in range(1, n + 1):
            if graph[i][j] or graph[j][i]:
                count_ += 1
        if count_ == n - 1:
            answer += 1

    return answer