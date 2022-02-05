# 메뉴 리뉴얼
# 2021 KAKAO BLIND RECRUITMENT
# 2022.02.04
# 16:35 ~ 17:30 (55 min)
# 후기 : combinations와 Conuter를 알면 풀기 쉬운 문제임.

from itertools import combinations
from collections import Counter

def solution(orders, course):
    answer = []
    for c in course:
        temp = []
        for order in orders:
            combi = combinations(sorted(order), c)
            temp += combi
        counter = Counter(temp)
        if len(counter) != 0 and max(counter.values()) != 1:
            answer += [''.join(f) for f in counter if counter[f] == max(counter.values())]

    return sorted(answer)