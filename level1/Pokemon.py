# 포켓몬
# 찾아라 프로그래밍 마에스터
# 2022.02.03
# 18:15 ~ 18:25 (10 min)
# 후기 : return min(len(set(nums)), len(nums)/2)으로 했으면 더 간단했음.
#       set을 이용하면 쉬운 문제임.

def solution(nums):
    return min(len([n for n in set(nums)]), len(nums)/2)