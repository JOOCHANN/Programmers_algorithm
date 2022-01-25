# 신고 결과 받기
# 2022 KAKAO BLIND RECRUITMENT
# 2022.01.25 
# 12:35 ~ 13:10 (35 min)
# 후기 : set을 이용하여 중복된 원소를 제거하면 더 효율적임

def solution(id_list, report, k):
    
    id_len = len(id_list)
    answer = [0 for i in range(id_len)]
    tmp = [[0 for i in range(id_len)] for j in range(id_len)]
    dic = {i : _ for _, i in enumerate(id_list)}
    
    for i in report:
        a = i.split(" ")
        tmp[dic[a[1]]][dic[a[0]]] = 1 
    
    for _, i in enumerate(tmp):
        num = i.count(1)
        
        if num >= k:
            i_idx = [__ for __, j in enumerate(i) if j == 1]
            for m in i_idx:
                answer[m] += 1

    return answer