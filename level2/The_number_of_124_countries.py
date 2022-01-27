# 124 나라의 숫자
# 연습문제
# 2022.01.27
# 14:25 ~ ( min)
# 후기 : 3의 배수인 케이스와 아닌 케이스를 구분하여 결과를 비교하였을때, 
#       3의 배수인 경우에 대해서는 1을 빼주는 것이 핵심 포인트

def solution(n):
    numbers = ['4', '1', '2']
    answer = ''

    while n:
        mok = n // 3
        na = n % 3
        answer = numbers[na] + answer
        n = mok - (na == 0)

    return answer