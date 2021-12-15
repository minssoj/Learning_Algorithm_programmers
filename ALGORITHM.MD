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

## 📌 DP

## 📌 최단경로
* 플루이드 워셜

## 📌 그래프 이론
