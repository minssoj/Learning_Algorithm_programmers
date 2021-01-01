# array = [[1, 2, 3],[4,5, 6],[7, 8, 9]]
# print(*array[::-1])
# roatated = list(zip(*array[::-1]))

# def union_parent(parent, a, b):
#     a = find_parent(parent, a)
#     b = find_parent(parent, b)
#
#     if a < b:
#         parent[b] = a
#     else:
#         parent[a] = b
#
#
# def find_parent(parent, a):
#     if parent[a] != a:
#         parent[a] = find_parent(parent, parent[a])
#     return parent[a]
#
#
# def solution(n, computers):
#     answer = 0
#     parent = [i for i in range(n)]
#
#     for i in range(n):
#         for j in range(n):
#             if i != j and computers[i][j] == 1:
#                 union_parent(parent, i, j)
#
#     # answer = set()
#
#     for i in range(n):
#         parent[i] = find_parent(parent, i);
#         # answer.add(parent[i])
#
#     return len(set(parent))


