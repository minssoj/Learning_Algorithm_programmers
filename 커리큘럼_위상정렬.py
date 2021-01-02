from collections import deque
import copy
def to_sort(n, indegree, time_, graph ):
    result = copy.deepcopy(time_)
    q = deque()
    # 진입차수가 0인 것
    for i in range(1, n+1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()
        for i in graph[now]:
            result[i] = max(result[i], result[now]+time_[i])
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)
    return result

def solution(n, cls):
    indegree = [0] * (n + 1)
    time_ = [0] * (n + 1)
    graph = [[] for _ in range(n+1)]

    # graph 만들기
    for i in range(n):
        data = cls[i]
        time_[i+1] = data[0]
        for j in data[1:-1]:
            indegree[i+1] += 1
            graph[j].append(i+1)
    # 위상정렬

    result = to_sort(n, indegree, time_, graph)
    return result[1:]

# answer : [10, 20, 14, 18, 17]
print(solution(5, [(10, -1), (10, 1, -1), (4,1, -1), (4, 3, -1), (3, 3, -1)]))