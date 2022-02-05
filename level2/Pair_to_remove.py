# 짝지어 제거하기
# 2017 팁스타운
# 2022.02.04
# 13:55 ~ 15:00 (65 min)
# 후기 : 시간초과를 해결해주기 위해 시간이 소요됨.
#       문자열을 하나씩 비교하는 것보다 stack을 쌓아서 하나씩 넣어두는 방법이 효과적임
#       문자열 슬라이싱으로 처리하는것보다 리스트를 만들어 pop 해주는것이 더 빠름.

def solution(s):
    stack = []
    
    for i in s:
        if not stack:
            stack.append(i)
        elif stack[-1] == i:
            stack.pop()
        else:
            stack.append(i)
            
    if len(stack) == 0:
        return 1
    
    return 0
        