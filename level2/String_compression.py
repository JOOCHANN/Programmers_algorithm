# 문자열 압축
# 2020 KAKAO BLIND RECRUITMENT
# 2022.01.26
# 14:00 ~ 15:21 (81 min)
# 후기 : 글자를 자를때 고려해주어할 부분이 생각보다 복잡했음. 너무 복잡하게 푼거같음. 
#       문자를 자르는 것을 반복문으로 그때그때 하나씩 만드는 것이 아니라 미리 일정한 토큰 사이즈로 잘라놓은 리스트를 만들어 두면 편했을듯함.

def solution(s):
    answer = 0
    len_s = len(s)
    half = int(len_s*0.5)+1
    res = []
    
    if len_s == 1:
        return 1
    
    for i in range(1, half):
        count = 1
        start_word = s[0:i]
        new_s = ''
        last = len_s-i+1
        
        for j in range(0, last, i):
            tmp = s[j+i:j+2*i]
            
            if start_word == tmp:
                count += 1
                if j >= last-i and j < last:
                    new_s += str(count) + start_word
            else:
                if count >= 2:
                    new_s += str(count) + start_word
                else:
                    new_s += start_word
                    
                start_word = tmp
                count = 1
                if j >= last-i and j < last :
                    new_s += start_word
                
        res.append(len(new_s))
        
    answer = min(res)
    return answer