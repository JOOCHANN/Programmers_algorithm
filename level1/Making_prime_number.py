# 소수 만들기
# Summer/Winter Coding(~2018)
# 2022.01.27
# 14:00 ~ 14:15 (15 min)
# 후기 : (from itertools import combinations) condition 함수를 활용했더라면 3중 for문을 할 필요가 없었음.

import math

def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def solution(nums):
    answer = 0
    n_l = len(nums)

    for i in range(n_l):
        for j in range(i+1, n_l):
            for k in range(j+1, n_l):
                if is_prime(nums[i]+nums[j]+nums[k]):
                    answer +=1 

    return answer