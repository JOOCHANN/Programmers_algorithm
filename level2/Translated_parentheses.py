# 괄호 변환
# 2020 KAKAO BLIND RECRUITMENT
# 2022.02.04
# 17:50 ~ 19:30 (100 min)
# 후기 : 재귀적으로 푸는 문제. 아직 재귀적 방법이 익숙치 않음.

from collections import Counter

def solution(p):
    # 1.
    if not p:
        return p
    # 2.
    u, v = n_2(p)
    # 3. 
    if is_right_3(u):
        return u + solution(v)
    else: # 4.
        # 4-1.
        answer = "("
        # 4-2.
        answer += solution(v)
        # 4-3.
        answer += ")"
        # 4-4.
        for p in u[1:-1]:
            if p == '(':
                answer += ')'
            else:
                answer += '('
        
    return answer

def n_2(p):
    u, v = '', ''
    len_p = len(p)
    half = len_p//2
    for i in range(2, len_p+1, 2):
        c = Counter(p[0:i])
        if c["("] == c[")"]:
            u += p[0:i]
            v = p[i:]
            break
    return u, v

def is_right_3(u):
    c = 0
    right_string = True
    for i in u:
        if i == "(":
            c+=1
        else:
            c-=1
        if c < 0:
            right_string = False
            
    return right_string