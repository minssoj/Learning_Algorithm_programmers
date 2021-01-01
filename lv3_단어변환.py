from collections import deque


def solution(begin, target, words):
    # 예제 2 케이스
    if target not in words:
        return 0

    q = deque()
    visited = []
    # visited = [False]* len(words)
    q.append((begin, 0))

    while q:
        node, num = q.popleft()
        visited.append(node)
        if node == target:
            return num
        num += 1
        for word in words:
            if word not in visited:
                d = 0
                for i, j in zip(word, node):
                    if i != j:
                        d += 1
                if d == 1:
                    q.append((word, num))
    return 0