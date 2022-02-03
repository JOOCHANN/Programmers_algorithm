# N으로 표현
# 동적계획법(Dynamic Programming)
# 2022.02.03
# 15:00 ~  ( min)
# 후기 : 총 8회 이하 까지만을 취급하기 때문에 8크기의 set을 만들어 두고,
#       첫번째에는 숫자 하나로 만들수 있는 값들, 두번째에는 숫자 두개로 만들 수 있는 것들 순으로 만드는 방법.
#       순서가 진행될수록 반복되는 연산이 진행될 수 있기 때문에 이전 set의 원소들을 조합하여 연산을 진행하는 것이 핵심.

def solution(N, number):
    if N == number:
        return 1
    
    answer = -1
    S = [set([int(str(N)*i)]) for i in range(1, 9)]
    
    for i in range(1, 8):
        for j in range(i):
            for o1 in S[j]:
                for o2 in S[i-j-1]:
                    S[i].add(o1+o2)
                    S[i].add(o1-o2)
                    S[i].add(o1*o2)
                    if o2 != 0 :
                        S[i].add(o1//o2)
        if number in S[i]:
            answer = i+1
            break
            
    return answer