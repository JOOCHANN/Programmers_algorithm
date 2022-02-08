# [1차] 뉴스 클러스터링
# 2018 KAKAO BLIND RECRUITMENT
# 2022.02.08
# 13:50 ~ 14:10 (20 min)
# 후기 : 먼저 문자열을 upper로 통일하고, 문자인지를 isalpha를 통해 확인후에 
#       문자 두개씩 나누어 리스트에 저장하는 방법이 핵심이었음.
#       str1_l, str2_l를 비교하면서 합집합, 교집합을 찾아 
#       아래 주석 코드와 같이 그 문자열을 카운트 해주면 좀더 간단했음.
# 
# def solution(str1, str2):
#     set1 = [str1[i:i+2].lower() for i in range(len(str1) - 1) if str1[i:i+2].lower().isalpha()]
#     set2 = [str2[i:i+2].lower() for i in range(len(str2) - 1) if str2[i:i+2].lower().isalpha()]

#     uu = sum([min(set1.count(u), set2.count(u)) for u in list(set(set1) & set(set2))])
#     nn = sum([max(set1.count(n), set2.count(n)) for n in list(set(set1) | set(set2))])

#     if nn == 0 and uu == 0:
#         return 65536
#     return int(float(uu)/float(nn) * 65536)

from collections import deque

def solution(str1, str2):
    answer = 65536
    len_str1, len_str2 = len(str1)-1, len(str2)-1
    str1, str2 = str1.upper(), str2.upper()
    str1_l = deque([str1[_:_+2] for _ in range(len_str1) if str1[_:_+2].isalpha()])
    str2_l = [str2[_:_+2] for _ in range(len_str2) if str2[_:_+2].isalpha()]
    inter = []
    union = []
    
    while str1_l :
        t = str1_l.popleft()
        if t in str2_l:
            inter.append([t])
            str2_l.remove(t)
        union.append([t])

    for s in str2_l:
        if s not in union:
            union.append([s])
            
    if union:
        answer = int((len(inter)/len(union))*65536)

    return answer