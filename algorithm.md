# algorithm

## 📌 목록
1.. BFS

1) Q에 시작점 넣고 2) 큐에서 빼서 연결된 유효한 노드 넣고 방문처리
ex. 단지번호 붙이기
```python
def bfs(x, y, cnt):
    q = deque()
    q.append((x, y))
    group[x][y] = cnt
    while q:
        x, y = q.popleft()
        
        # 위 아래 왼쪽 오른쪽 탐색
        for k in range(4):
            nx, ny = x+dx[k], y+dy[k]
            # 지도 밖으로 안 나갔는지 확인
            if 0<=nx<n and 0<=ny<n :
                # 집이 있고, 아직 방문한 곳이 아니라면 꼬우
                if a[nx][ny] == 1 and group[nx][ny] == 0:
                    q.append((nx, ny))
                    group[nx][ny] = cnt

cnt = 0
for i in range(n):
    for j in range(n):
        if a[i][j] == 1 and group[i][j] == 0:
            cnt += 1
            bfs(i, j, cnt)

```

2.. DFS (재귀함수 및 stack으로 구현 가능)

0) dfs 구현 (방문처리, 유효하고 연결되어 있는 방문처리 되지 않은 노드로 가서 dfs호출) 1) visited 만들기 2) 처음 시작부분에서 dfs 호출
```python
def dfs(root, visited, computers):
    visited[root] = True # 방문여부 표시
    for i in range(len(visited)): # len(visited) = n
        # root-i를 잇는 간선이 있고, 정점i를 아직 방문 안했다면
        if computers[root][i] and not visited[i]: 
            computers[root][i], computers[i][root] = 0, 0 # 간선 방문후 삭제(무방향그래프니까, 양쪽 모두 변경)
            dfs(i, visited, computers) # 정점i의 이웃노드 탐색을 위해 dfs()호출

def solution(n, computers):
    answer = 0 # 네트워크 개수
    visited = [False]*n # 방문여부 판단
    for i in range(n):
        if not visited[i]: # 아직 방문하지 않은 정점
            dfs(i, visited, computers) 
            answer += 1 # 네트워크 개수 증가
    return answer
```

3.. DP
```python

```

4.. 크루스칼

1) edge 비용별로 sort 2) 같은 집합 아니면 비용 추가 하고 같은 집합으로 만들기
```python
def find_parent(parent, a):
    if parent[a] != a:
        parent[a] = find_parent(parent, parent[a])
    return parent[a]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

def solution(n, costs):
    parent = [i for i in range(n)]
    edge_q = []
    answer = 0

    for a, b, c in costs:
        edge_q.append((c, a, b))

    # 짧은 간선부터 연결
    edge_q.sort()

    for c, a, b in edge_q:
        # 같은 집합이면 skip,
        if find_parent(parent, a) == find_parent(parent, b):
            continue
        # 다른 집합이면, 집합 합치고, 비용에 추가
        union_parent(parent, a, b)
        answer += c

    return answer
```

5.. 위상정렬

1) 큐에 진입차수 0인 것을 넣는다. 2) 방문 후 진입차수 제거  다시 1)부터
```python
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
```
6.. 다익스트라
```python
# 방문하지 않은 노드 중에 가장 짧은 거리 선택
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
```
7.. 플로이드 워셜
```python
# j에서 i를 거쳐서 k를 가능 경우를 고려
for i in range(1, n + 1):
    for j in range(1, n + 1):
        for k in range(1, n + 1):
             graph[j][k] = min(graph[j][k], graph[j][i] + graph[i][k])

# j에서 i를 i에서 k를 가는것이 가능하면 j에서 k가는 것이 가능
for i in range(1, n + 1):
    for j in range(1, n + 1):
        for k in range(1, n + 1):
            if graph[j][i] and graph[i][k]:
                graph[j][k] = True
```
8.. 이분탐색

예산 : https://jisun-rea.tistory.com/entry/python-%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-Level3-%EC%98%88%EC%82%B0-%EC%9D%B4%EB%B6%84%ED%83%90%EC%83%89
```python
def solution(budgets, M):
    ans = 0
    left = 0
    right = M
    max_total = 0
    if sum(budgets)<=M:
        return max(budgets)
    while left<right-1:
        mid = (left+right)//2
        total = 0
        for b in budgets:
            if b < mid:
                total += b
            else:
                total += mid
        if total<=M:
            left = mid
            if total>max_total:
                max_total = total
                ans = mid
        else:
            right = mid
    return ans
```

9.. LIS : 가장 긴 증가하는 부분 순열
```python
from bisect import bisect_left
def solution(a):
    L = []
    P = []
    # P, L 찾기
    for idx, i in enumerate(a):
        if idx == 0 or L[-1] <= i:
            L.append(i)
            pos = bisect_left(L, i)
        else:
            pos = bisect_left(L, i)
            L[pos] = i
        P.append(pos)

    # 실제 수열 찾기
    answer = []
    idx = len(L) -1
    for i in range(len(a)-1, -1, -1):
        if idx < 0:
            break
        if P[i] == idx:
            answer.append(a[i])
            idx -= 1
    answer.reverse()
    return answer
print(solution([3, 2, 5, 2, 3, 1, 4]))
```

10.. 해시
```python
def solution(genres, plays):
    song = dict()
    num_play = dict()
    answer = []

    for i in range(len(genres)):
        # 장르 내부 정렬을 위해 song에 삽입
        genre = genres[i]
        play = plays[i]
        if genre in song:
            song[genre].append([-1 * play , i ])
            song[genre].sort()
        else:
            song[genre] = [[(-1) * play , i ]]
        
        # 장르 순위를 매기기 위한 플레이수 합
        if genre in num_play:
            num_play[genre] += play
        else:
            num_play[genre] = play
        
    # 장르별로 줄 세우고, 그 장르 안에서 2개 추출
    genre_p = []
    for genre in num_play.keys():
        genre_p.append([num_play[genre],genre])
    genre_p.sort(reverse=True)
    
    for _, genre in genre_p:
        for i in range(2):
            answer.append(song[genre][i][1])
            if len(song[genre]) == 1:
                break
    return answer
```

## 📌 주로 쓰는 라이브러리
```python
