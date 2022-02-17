# 3진법 뒤집기
# 월간 코드 챌린지 시즌1
# 2022.02.17
# 14:12 ~ 14:32 (20 min)
# 후기 : int(tmp, 3) 와 같이 int()안에 뒤 인자를 3으로 입력하면 
#       3진 수로 표현한 수를 10진 수로 표현할 수 있음을 알게됨.
#       while 문으로 3을 나눈 목을 계속 확인해줬으면 굳이 재귀함수가 필요없음.

def solution(n):
    answer = 0
    if n < 3:
        return n
    r = make_ternary(n, '')
    li = list(r)
    for _, l in enumerate(li):
        answer += 3**_ * int(l)

    return answer

def make_ternary(num, result):
    na = num % 3
    mok = num // 3
    result = str(na) + result
    
    if mok < 3:
        result = str(mok) + result
        return result
    else:
        result = make_ternary(mok, result)
    return result
    
    
    