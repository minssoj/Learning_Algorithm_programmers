# TEMPLATE

## 📌 주로 쓰는 라이브러리
```python
import sys                          # 대량 입력 받을 때
from collections import deque       # 큐, 스택
import math                         # 제곱근, 팩토리얼
import heapq                        # 힙, 우선순위 큐
from itertools import permutations, combinations, product, combinations_with_replacement  # 순열, 조합
from collections import Counter                     # 카운터
from collections import defaultdict                 # defaultdict
from bisect import bisect_left, bisect_right        # 이진탐색    
import re
from functools import cmp_to_key
```

## 📌  입력
* Ex. 기본 입력
```python
l = list(map(int, input().split))   # list에 입력 저장
n, m = map(int, input().split)      # 여러 변수에 입력 저장
```
* Ex. 줄바꿈 제거 후 입력
```python
import sys
data = sys.stdin.readline().rstrip()
```
* Ex. 많은 입력 받기 (시간초과 방지)
```python
import sys
input = sys.stdin.readline
n, m = map(int, input().split)      # 여러 변수에 입력 저장
```

## 📌 String
* Ex.문자열 리스트로 저장
```python
s = 'abcd'
l = list(map(int, s))           # 기존 문자열 리스트변환
l_1 = list(map(int, input()))   # 입력받은 문자열 리스트변환
l = list(map(str, s))           # 분리하여 리스트화
```
* Ex.리스트로 문자열
```python
# 주의 : 숫자 문자열
l = [1,2,3,4]
s = str(int(''.join(l)))
```
* Ex. 기타
```python
s = 'abcd'
s.replace('?','a')      # 대체
s.split("},{")          # 분할

s.count('1', 0, 3)
```

## 📌 Array
* Ex. 2차원 배열 초기화
```python
n, m = 2, 3
a = [[0]*n for _ in range(m) ]
```

* 열별로 묶기
```python
for B_col in zip(*B)
```

* Ex. 행렬 뒤집기
```python
array = [[1, 2, 3],[4,5, 6],[7, 8, 9]]
reversed = list(map(list,zip(*array)))
```

* Ex. 90도 회전 ver1
```python
array = [[1, 2, 3],[4,5, 6],[7, 8, 9]]
roatated = list(zip(*array[::-1]))
```
* Ex. 회전 90도 단위로 (https://shoark7.github.io/programming/algorithm/rotate-2d-array)
```python
def rotate(m, d):
    """2차원 배열을 90도 단위로 회전해 반환한다.
       이때 원 배열은 유지되며, 새로운 배열이 탄생한다. 이는 회전이 360도 단위일 때도 해당한다.
       2차원 배열은 행과 열의 수가 같은 정방형 배열이어야 한다.

       :input:
       m: 회전하고자 하는 2차원 배열. 입력이 정방형 행렬이라고 가정한다.
       d: 90도씩의 회전 단위. -1: -90도, 1: 90도, 2: 180도, ...
    """
    N = len(m)
    ret = [[0] * N for _ in range(N)]

    if d % 4 == 1: 
        for r in range(N): 
            for c in range(N): 
                ret[c][N-1-r] = m[r][c]
    elif d % 4 == 2:
        for r in range(N):
            for c in range(N):
                ret[N-1-c][N-1-r] = m[r][c]
    elif d % 4 == 3:
        for r in range(N):
            for c in range(N):
                ret[N-1-c][r] = m[r][c]
    else:
        for r in range(N):
            for c in range(N):
                ret[r][c] = m[r][c]

    return ret
```

## 📌 Queue, Stack
### Queue
* Ex. deque 이용
```python
from collections import deque
# 1. 초기화
q = deque([1,2,3])
# 2. 삽입
q.append(4)
# 3. 삭제
q.popleft()
# 4. 조회
q[0]
```
* Ex. list 이용
```python
# 1. 초기화
p = [1, 2, 3]
# 2. 삽입
p.append(4)
# 3. 삭제
p.pop(0)
```
### Stack
* Ex. deque 이용
```python
from collections import deque
# 1. 초기화
s = deque([1,2,3])
# 2. 삽입
s.append(4)
# 3. 삭제
s.pop()
# 4. 조회
s[0]
```
* Ex. list 이용
```python
# 1. 초기화
s = [1,2,3]
# 2. 삽입
s.append(4)
# 3. 삭제
s.pop()
```

## 정렬
* Ex. 내장함수 (sort)
```python
l = [[1, 4],[2, 3],[3, 2],[4, 1]]
l.sort()                                            # 오름차순                
l.sort(reverse=True)                                # 내림차순
```
* Ex. 내장함수 (sorted)
```python
l = [[1, 4],[2, 3],[3, 2],[4, 1]]
sorted(l)                                            # 오름차순                
sorted(l, reverse=True)    # 내림차순
sorted(l, key= lambda x : x[1], reverse=True)     # 기준, 내림차순
```

## 📌 Heap
* Ex. heapq 기반
```python
import heapq
l = [1,2,3]
# 1. 초기화
pq = heapq.heapify(l)
# 2. 삽입
heapq.heappush(pq, -1)
# 3. 제거
heapq.heappop(pq)
# 4. 조회
pq[0]
```
* Ex. 리스트 기반 우선순위 큐
```python
# 1. 초기화
l = list()
# 2. 삽입
l.append(1)
l.sort(key =lambda x:x[0])
# 3. 출력
l.pop(0)
```

## 📌 Dictionary
```python
# 1. 해쉬 초기화
h = {}
h1 = dict()
# 2. 삽입
h['total'].append(160)
# 3. get
h['total']
h.get('total',0)
# 4. 제거
h.pop('A', 180)
# 5. 탐색
h.items()
h.keys()
h.values()
```

## 📌 집합
```python
# 1. 초기화
s1 = set()
s2 = set()
# 2. 삽입
s1.add(1)
s2.add(2)
# 3. 제거
s1.remove(1)
# 4. 합집합, 교집합, 차집합
s1 | s2
s1 - s2
s1 & s2
```

## 📌 순열, 조합
```python
from itertools import permutations, combinations, product, combinations_with_replacement
data = ['A', 'B', 'C']
result_p = list(permutations(data,2))
result_c = list(combinations(data,2))
result_pp = list(product(data,2))
result_cc = list(combinations_with_replacement(data, 2))
```

## 📌 기타
* 조건부 표현식
```python
score = 85
result = "sucess" if score >= 80 else "fail"
```
* list comprehension
```python
a = [1, 2, 3, 4, 5, 5, 5]
remove_set = {3, 5}
result = [i for i in a if i not in remove_set]
```
* counter
```python
from collections import Counter  
a = [1, 2, 3, 4, 5, 5, 5]
Counter(a)
```
* bisect
```python
from bisect import bisect_left, bisect_right
l = [1,2,3,4,4,5]
start = 4
end = 5
bisect_left(l, start)       # 최소값 들어갈 index
bisect_right(l, end)        # 최대값 들어갈 index
```
* 아스키코드
```python
ord('A')
chr()
```
* 정규 표현식
```python
# 숫자 : \d, 공백: \s, 문자 +숫자 : \w
a.b     # a + 모든 문자 + b
ca*t    # a 0회이상
ca+t    # a 1회 이상
ca{2,5}t# a 2 ~5회
ca?t    # a 있어도 없어도
import re
p = re.compile('ab*')
m = p.match("python")
print(m.group)
m = p.search("python")  # match와의 차이점 : 처음부터 하는 것이 아니다
result = p.findall("life is too short")

file_num = sorted(input_, key=lambda x : int(re.findall('\d+', x)[0]))
final = sorted(file_num, key=lambda x : re.split('\d+', x.lower())[0])
```
* 정렬 tip - cmp_to_key
```python
from functools import cmp_to_key
def func(a,b):
    return 1 # 1이면 b를 앞으로, -1이면 a를 앞으로
sorted(l, key=cmp_to_key(func))
```
* Ex.
```python
#최대공약수:
import math
def gcd_(a, b):
    if a % b == 0: return b 
    else: return gcd_(b, (a % b))
math.gcd(x,y)
#최소공배수:
math.lcm(x,y)
x*y//math.gcd(x,y)
```



# ---
* Ex.
```python

```



## 예시
*해시
```python
def solution(genres, plays):
    song = dict()
    num_play = dict()
    answer = []

    for i in range(len(genres)):
        # 장르 내부 정렬을 위해 song에 삽입
        genre = genres[i]
        play = plays[i]
        if genre in song:
            song[genre].append([-1 * play , i ])
            song[genre].sort()
        else:
            song[genre] = [[(-1) * play , i ]]
        
        # 장르 순위를 매기기 위한 플레이수 합
        if genre in num_play:
            num_play[genre] += play
        else:
            num_play[genre] = play
        
    # 장르별로 줄 세우고, 그 장르 안에서 2개 추출
    genre_p = []
    for genre in num_play.keys():
        genre_p.append([num_play[genre],genre])
    genre_p.sort(reverse=True)
    
    for _, genre in genre_p:
        for i in range(2):
            answer.append(song[genre][i][1])
            if len(song[genre]) == 1:
                break
    return answer
```