import heapq
def dsr(start, graph, distance):
    q = []
    distance[start] = 0
    heapq.heappush(q, (0, start))
    while q:
        dist, now = heapq.heappop(q)
        # 방문 확인
        if distance[now] < dist:
            continue
        # 인접 노드 확인
        for i in graph[now]:
            cost = dist + 1
            # 업데이트 사항 있으면 q에 넣어주기
            if cost < distance[i]:
                distance[i] = cost
                heapq.heappush(q, (cost, i))

def solution(n, edge):
    graph = [[] for i in range(n + 1)]
    distance = [int(1e9)] * (n + 1)

    # graph 완성
    for e in edge:
        graph[e[0]].append(e[1])
        graph[e[1]].append(e[0])

    dsr(1, graph, distance)

    distance.remove(int(1e9))
    return distance.count(max(distance))