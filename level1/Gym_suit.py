# 체육복
# 탐욕법
# 2022.02.03
# 11:55 ~ 12:35 (40 min)
# 후기 : n의 최대 크기가 30이기 때문에 체육복 정보가 담긴 딕셔너리를 생성하였음, 
#       그리고 체육복이 없는 학생의 앞뒤 학생중 여벌이 있는 경우 주도록 하였음.
#       딕셔너리를 생성하지 않고, reserve 정보만으로 lost안에 있는 학생들의 
#       앞뒤를 살펴보고 코딩할 수 있었음. 이것이 더 효율적이었을듯.

def solution(n, lost, reserve):
    dic = {}
    
    for i in range(1, n+1):
        if i in lost:
            if i in reserve:
                dic[i] = 1
            else:
                dic[i] = 0
        else:
            if i in reserve:
                dic[i] = 2
            else:
                dic[i] = 1

    for k, v in dic.items():
        if v == 0:
            if k-1 in dic.keys():
                if dic[k-1] > 1:
                    dic[k] = 1
                    dic[k-1] -= 1
            if k+1 in dic.keys():
                if k <= n and dic[k+1] > 1:
                    dic[k] = 1
                    dic[k+1] -= 1
                    
    return sum([1 for v in dic.values() if v >= 1])