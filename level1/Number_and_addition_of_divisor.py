# 약수의 개수와 덧셈
# 월간 코드 챌린지 시즌2
# 2022.02.17
# 14:00 ~ 14:06 (6 min)
# 후기 : 약수의 개수를 만들어 주는 함수를 만들어 두면 쉬움
#       제곱수라면 약수의 개수가 홀수가됨 이것을 알았더라면 약수의 개수를 반환하는 함수가 필요없음
#       예를 들어 16의 약수는 1, 2, 4, 8, 16 으로 제곱수 이기 때문에 4가 들어가 홀수가됨.

def solution(left, right):
    answer = 0
    
    for i in range(left, right+1):
        number = num_divisor(i)
        if number%2==0:
            answer += i
        else:
            answer -= i
    
    return answer

def num_divisor(number):
    result=0
    for i in range(1, number+1):
        if number%i==0:
            result+=1
            
    return result
