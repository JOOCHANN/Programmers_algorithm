# 타겟 넘버
# 깊이/너비 우선 탐색(DFS/BFS)
# 2022.01.28
# 13:50 ~ 14:25 (35 min)
# 후기 : 아래와 같이 product와 map을 활용했더라면 좀더 간편했을듯.
#
# from itertools import product
# def solution(numbers, target):
#     l = [(x, -x) for x in numbers]
#     s = list(map(sum, product(*l)))
#     return s.count(target)

from collections import deque

def solution(numbers, target):
    q = deque(numbers)
    first = q.popleft()
    v = [first, -first]

    while q:
        cur = q.popleft()
        tmp = []
        for _ in v:
            tmp.append(_ + cur)
            tmp.append(_ - cur)

        v = tmp

    return v.count(target)