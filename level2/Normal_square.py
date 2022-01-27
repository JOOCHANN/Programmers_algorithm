# 멀쩡한 사각형
# Summer/Winter Coding(2019)
# 2022.01.27
# 12:40 ~ 13:30 (50 min)
# 후기 : 최대공약수를 활용하는것 까지는 생각을 했는데, 그 이후 방법에서 시간이 오래걸렸음.
#       w*h-w-h+gcd(w,h)가 더 간단하던데 왜 이렇게 더 간단한지 내가 푼 방법의 식을 정리해보고서야 알게됨.
#       한번에 저렇게 떠올릴 수있나? 싶었음...

import math

def solution(w,h):
    answer = w*h

    if w == h:
        return answer - w

    b = math.gcd(w, h)
    b_w = int(w/b)
    b_h = int(h/b)
    re = int(max([w, h]) / max(b_w, b_h))

    return answer - (b_w + b_h - 1) * re