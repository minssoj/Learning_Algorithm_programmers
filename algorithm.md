# algorithm

## 📌 목록
1. BFS

2. DFS

3. DP

4. 크루스칼

5. 위상정렬

6. 다익스트라

7. 플로이드 워셜

8. 해시

9. 이진탐색


10. LIS : 가장 긴 증가하는 부분 순열
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
## 📌 주로 쓰는 라이브러리
```python
