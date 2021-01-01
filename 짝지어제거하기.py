def solution(s):
    l = []
    for i in s:
        if l and l[-1] == i:
            l.pop()
        else:
            l.append(i)

    if len(l) == 0:
        return 1
    else:
        return 0

input = ["baabaa"]

for i in input:
    print(solution(i))