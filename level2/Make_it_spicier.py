# 기능개발
# 스택/큐
# 2022.01.27
# 18:35 ~ 19:10 (35 min)
# 후기 : 리스트의 최소값을 찾으려고 sort()를 사용하다보니 타임아웃이 발생해, heapq를 사용하게 되었음.
#       heapq를 처음 알게되었고, 리스트의 최소값을 찾는데에는 heapq가 효과적이라는것을 알게됨.

import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    min_s = scoville[0]

    while min_s < K :
        if len(scoville) == 1:
            return -1

        answer += 1
        new = heapq.heappop(scoville) + heapq.heappop(scoville) * 2

        heapq.heappush(scoville, new)

        min_s = scoville[0]

    return answer