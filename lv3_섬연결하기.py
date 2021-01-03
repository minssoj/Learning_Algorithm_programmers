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