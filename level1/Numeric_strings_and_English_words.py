# 숫자 문자열과 영단어
# 2021 카카오 채용연계형 인턴십
# 2022.01.25
# 16:15 ~ 16:22 (7 min)
# 후기 : 그냥 쉬웠다. while 문이 굳이 없었어도 됐을거같다.

def solution(s):
    answer = 0
    
    number = {0:'zero', 1:'one', 2:'two', 3:'three', 4:'four', 
              5:'five', 6:'six', 7:'seven', 8:'eight', 9:'nine'}
    
    while not(s.isdigit()) :
        for i in range(10):
            s = s.replace(number[i], str(i))
    
    answer = int(s)
    return answer