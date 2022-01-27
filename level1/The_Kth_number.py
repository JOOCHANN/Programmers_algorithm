# K번째 수
# 정렬
# 2022.01.27
# 19:15 ~ 19:18 (3 min)
# 후기 : 쉬웠음. sort()말고 sorted 함수를 사용했더라면 반복문을 한줄로 표현 가능 했을듯

def solution(array, commands):
    answer = []
    
    for (i, j, k) in commands:
        tmp = array[i-1:j]
        tmp.sort()
        answer.append(tmp[k-1])
        
    return answer