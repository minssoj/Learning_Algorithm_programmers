import heapq
INF = int(1e9)
def dsr(s, graph, distance):
    q = []
    heapq.heappush(q, (0, s))
    distance[s] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for c, i in graph[now]:
            cost = dist + c
            if cost < distance[i]:
                distance[i] = cost
                heapq.heappush(q, (cost, i))

def solution(N, road, K):
    answer = 0
    graph = [[] for i in range(N + 1)]
    distance = [INF] * (N + 1)
    for a, b, c in road:
        graph[a].append((c, b))
        graph[b].append((c, a))

    for i in graph:
        i.sort()
    dsr(1, graph, distance)
    for i in range(1, N + 1):
        if distance[i] >= 0 and distance[i] <= K:
            answer += 1
    return answer