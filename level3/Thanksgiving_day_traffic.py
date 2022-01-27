# [1차] 추석 트레픽
# 2018 KAKAO BLIND RECRUITMENT
# 2022.01.27
# 20:30 ~ 21:27 (57 min)
# 후기 : 시 분 초에서 초단위 작업 문제는 초로 바꾸는 작업이 수월함을 느낌. 
#       연산을 진행할때 round를 안써주니 쓰레기값이 뒤에 추가되어 방해가 되었음.
#       2중 for문을 안쓰고 해결할 수 있는 방법을 고민해봤지만, 찾지 못했음. 

def solution(lines):
    start_end = []
    len_l = len(lines)
    if len_l == 1:
        return 1
    
    for l in lines:
        l = l.split(" ")
        s, t = l[1].split(":"), l[2].split("s")[0]
        s = float(s[0]) * 3600 + float(s[1]) * 60 + float(s[2])
        
        if float(t) == 0.001:
            s0 = round(float(s), 4)
        else:
            s0 = round(float(s) - float(t) + 0.001, 4)
        
        start_end.append([s0, s])

    r = []
    
    for _ in range(len_l):
        tmp = 1
        for i in range(_+1, len_l):
            if start_end[_][1] >= round(start_end[i][0] - 0.999, 4):
                tmp += 1
        
        r.append(tmp)
    
    return max(r)