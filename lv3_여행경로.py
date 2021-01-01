# def dfs(tickets, used, ans):
#     print(ans)
#     if len(ans) == len(tickets) + 1:
#         return ans
#     else:
#         for ticket in tickets:
#             print(ticket not in used)
#             print(ans, ticket[0] == ans[-1])
#             if ticket not in used and ticket[0] == ans[-1]:
#                 used.append(ticket)
#                 ans.append(ticket[1])
#                 suc = dfs(tickets, used, ans)
#                 if suc:
#                     return suc
#                 used.remove(ticket)
#                 ans.remove(ticket[1])
#         return
#
#
# def solution(tickets):
#     ans = []
#     # 예제 2 해결하기 위해
#     tickets.sort()
#     used = []
#     ans.append("ICN")
#
#     if len(ans) == len(tickets) + 1:
#         return ans
#
#
#
#     return dfs(tickets, used, ans)

# print(solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]))
# print(solution([["ICN", "A"], ["A", "C"], ["A", "D"], ["D", "B"], ["B", "A"]]))
# print(solution([["ICN","A"],["ICN","A"],["A","ICN"]]))

# 중복 ticket 처리 불가로 위 코드 폐기

def solution(tickets):
    # ticket 저장 dictionary 중복 티켓도 사용하기 위해
    tk = dict()
    for ticket in tickets:
        if ticket[0] in tk:
            tk[ticket[0]].append(ticket[1])
        else:
            tk[ticket[0]] = [ticket[1]]

    for k in tk.keys():
        tk[k].sort(reverse=True)

    st = ["ICN"]
    answer = []
    while st:
        top = st[-1]
        if top not in tk or len(tk[top]) == 0:
            answer.append(st.pop())
        else:
            st.append(tk[top][-1])
            tk[top].pop()
    answer.reverse()
    return answer