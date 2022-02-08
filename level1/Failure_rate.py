# 실패율
# 2019 KAKAO BLIND RECRUITMENT
# 2022.02.08
# 12:40 ~ 13:20 (40 min)
# 후기 : total이 0이 되는 경우를 생각해주느라 시간이 좀 걸림
#       Counter를 사용하면 편리함.

from collections import Counter

def solution(N, stages):
    answer = []
    c = Counter(stages)
    total = len(stages)
    result = {}
    for n in range(N):
        if total :
            v = c[n+1]/total  
        else :
            v = 0
            
        if v in result:
            result[v] += [n+1]
        else:
            result[v] = [n+1]
        total -= c[n+1]

    key = sorted(list(result.keys()))[::-1]
    for k in key:
        answer += result[k]

    return answer