# 음양 더하기
# 월간 코드 챌린지 시즌2
# 2022.01.27
# 11:20 ~ 11:25 (5 min)
# 후기 : 너무 쉬웠음.

def solution(absolutes, signs):
    answer = 0
    for a, s in zip(absolutes, signs):
        if s: answer += a
        else: answer += -a

    return answer


