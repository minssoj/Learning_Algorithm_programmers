# ALGORITHM TEMPLATE

## 📌 완전탐색
* DFS (재귀함수)
  * 방문표시, 출력 or 연산, 다른 노드 방문
  * 종료 조건 필요 (예를 들어 좌표계 벗어남)
```python
def dfs(graph, v, visited):
  # 종료 조건 필요
  visited[v] = True
  print(v, end = ' ')
  for i in graph[v]:
    if not visited[i]:
      dfs(graph, i, visited)
```

* BFS (큐)
  * 큐 생성, 방문표시, 큐가 빌때까지 방문하지 않은 원소들 큐에 삽입
```python
def bfs(graph, start, visited):
  queue = deque([start])
  visited[start] = True
  
  while queue:
    v = queue.popleft()
    print(v, end = ' ')
    for i in graph[v]:
      if not visited[i]:
        queue.append(i)
        visited[i] = True
```

## 📌 정렬
```python
result = sorted(result, key = lambda x: x[1])
result.sort(key = lambda x : x[1], reverse = True)
```

## 📌 이진탐색
* 함수
```python
def binary_search(array, target, start, end):
  while start <= end:
    mid = (start + end) // 2
    if array[mid] == target:
      return mid
    elif array[mid] > target
      end = mid -1
    else:
      start = mid + 1
  return None
```

## 📌 최단경로
* 다익스트라
  * 특정노드 -> 모든 노드
  * `음의 간선` 없을때
  * Version 1
  ```python
  # version 1
  def get_smallest_node():
    min_value = INF
    index = 0
    for i in range(1, n+1):
      if distance[i] < min_value and not visited[i]:
        min_value = distance[i]
        index = i
    return index

  def dijkstra(start):
    distance[start] = 0
    visited[start] = True

    for j in graph[start]:
      distance[j[0]] =j[1]

    for i in range(n-1):
      now = get_smallest_node()
      visited[now] = True

      for j in graph[now]:
        cost = distance[now]+j[1]
        if cost <distance[j[0]]:
          distance[j[0]] = cost
  ```
  * Version 2
  ```python
  def dijkstra(start):
  q = []
  heapq.heappush(q, (0, start))
  distance[start]  = 0 

  while q:
    dist, now = heapq.heappop(q)
    if distance[now] < dist:
      continue
    for i in graph[now]:
      cost = dist + i[1]
      if cost <distance[i[0]]:
        distance[i[0]] = cost
        heapq.heappush(q, (cost, i[0]))
  ```
  
* 플루이드 워셜
```python
for k in range(1, n+1):
  for a in range(1, n+1):
    for b in range(1, n+1):
      graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])
```

## 📌 그래프 이론
* 서로소
  * 특정 원소가 속한 집합 찾기 (루트 노드 찾기)
  ```python
  def find_parent (parent , x ) :
    if parent [x] != x:
        parent [x] = find_parent(parent, parent[x])
    return parent[x]
  ```
  * 집합 합치기
  ```python
  def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b
  ```
* 크루스칼 알고리즘
```python
edge.sort()
for edge in edges:
    cost, a, b = edge
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost
```
* 위상정렬
```python
def topology_sort():
    result = []
    q = deque()
    
    for i in range(1, v+1):
        if indegree[i] == 0:
            q.append(i)
    
    while q:
        now = q.popleft()
        result.append(now)
        
        for i in graph[now]:
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)
```
