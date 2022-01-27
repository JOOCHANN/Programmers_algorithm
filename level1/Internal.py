# 내적
# 월간 코드 챌린지 시즌1
# 2022.01.27
# 11:32 ~ 11:34 (2 min)
# 후기 : 너무 쉬웠음.

def solution(a, b):
    return sum(x*y for x, y in zip(a, b))