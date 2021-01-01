def solution(name):
    answer = 0
    l = [min(ord(s)- ord('A') , ord('Z')- ord(s)+1) for s in name]
    answer += sum(l)

    # 위치에 대한 것
    if 0 not in l:
        answer += len(l)-1
        return answer

    locate = 0

    while True:
        l[locate] = 0
        if sum(l) == 0: break

        left = 1
        right = 1

        while l[locate+right] == 0:
            right += 1
        while l[locate - left] == 0:
            left += 1

        if left >= right:
            answer += right
            locate += right
        else:
            answer += left
            locate -= left

    return answer


input = ["JEROEN", "JAN"]

for i in input:
    print(solution(i))
