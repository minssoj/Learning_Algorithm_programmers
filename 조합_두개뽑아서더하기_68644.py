from itertools import combinations

def solution(numbers):
    answer = []
    for a, b in list(combinations(numbers,2)):
        if a+b not in answer:
            answer.append(a+b)
    answer.sort()
    return answer

example =[2,1,3,4,1]
print(solution(example))