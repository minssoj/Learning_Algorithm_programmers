from collections import deque
def solution(arr):
    # bfs로 풀이하기
    N = len(arr)
    visited = [False] * N
    q = deque()
    q.append((N-1, 0))

    while q:
        temp = q.popleft()
        now = temp[0]
        ans = temp[1]
        visited[now] = True
        print(now)
        if now == 0:
            return ans
        for i in range(len(arr)):
            if abs(now -i) == arr[i] and not visited[i]:
                q.append((i, ans+1))
    return -1

i = [[4, 1,2, 3, 1, 0, 5]]
for x in i:
    print(solution(x))