# 키패드 누르기
# 2020 카카오 인턴십
# 2022.01.26
# 16:15 ~ 16:48 (33 min)
# 후기 : keypad 번호를 좌표와 매핑되도록 딕셔너리를 미리 생성하였으면, 연산자 없이 더 수월하게 풀었을듯 함.

def solution(numbers, hand):
    answer = ''
    left_area = [1, 4, 7]
    right_area = [3, 6, 9]
    center = [2, 5, 8, 0]
    left_q = [3, 0] # Left start
    right_q = [3, 2] # Right start

    for n in numbers:
        if n in left_area:
            answer += "L"
            left_q = [n//3, 0]
        elif n in right_area:
            answer += "R"
            right_q = [n//3-1, 2]
        elif n in center:
            if n != 0: n_location = [n//3, 1]
            else : n_location = [3, 1]
            
            n_l = abs(n_location[0] - left_q[0]) + abs(n_location[1] - left_q[1])
            n_r = abs(n_location[0] - right_q[0]) + abs(n_location[1] - right_q[1])
            
            if (n_l == n_r and hand == "left") or (n_l < n_r):
                answer += "L"
                left_q = n_location
            elif (n_l == n_r and hand == "right") or (n_l > n_r):
                answer += "R"
                right_q = n_location
        
    return answer