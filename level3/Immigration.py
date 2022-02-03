# 입국심사
# 이분탐색
# 2022.02.03
# 15:40 ~ 17:30 (110 min)
# 후기 : 이분탐색을 하지 않고 풀었을때 시간초과로 인해 어려움이 있었음.
#       이분탐색을 찾아보고 풀었을때는 훨신 간단했고, 시간 단축이 빨랐음.
#       중간 값을 times의 원소들로 나눠서 개수를 확인하는 부분이 생각하기 어려웠음.

def solution(n, times):
    l = min(times)
    r = min(times)*n
    answer = 0
    
    while l <= r:
        m = (l+r)//2
        p = 0
        for t in times:
            p += m//t
        if p >= n:
            answer = m
            r = m-1
        elif p < n:
            l = m+1
        
    return answer