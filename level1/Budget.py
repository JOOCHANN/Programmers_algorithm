# 예산
# Summer/Winter Coding(~2018)
# 2022.02.17
# 14:40 ~ 15:10 (30 min)
# 후기 : 처음에는 예산들의 조합으로 풀려고했으나 시간 복잡도 측면에서 아래와 같이 다시 품.
#       d의 크기가 1인 경우와 모든 d의 합이 예산보다 작을 경우를 체크하는 것이 중요했음.

def solution(d, budget):
    answer = 0
    d.sort()
    d_len = len(d)
    
    if d_len == 1:
        if d[0] < budget:
            return 1
        
    if sum(d) < budget:
        return d_len
    
    for _, i in enumerate(d):
        budget -= i
        if budget == 0:
            return _+1
        elif budget < 0:
            return _