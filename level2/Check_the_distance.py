# 거리두기 확인하기
# 2021 카카오 채용연계형 인턴십
# 2022.02.08
# 15:10 ~ 15:55 (45 min)
# 후기 : 모든 P의 위치를 p_place에 저장하고,
#       p_place에서 두개를 뽑아 맨하튼 거리를 비교하여 2이상인 경우에는
#       그 사이에 존재하는 모든 좌표에 대해 살펴보고 O가 존재한다면 
#       거리두기를 지키지 않은 것으로 간주하고 0을 반환하도록함. 
#       그리고 길이가 2인경우도 PP인 경우이기 때문에 이 부분도 0으로 반환하도록함.

def solution(places):
    return [check(p) for p in places]

def check(place):
    place = [list(i) for i in place]
    p_place = [[x, y] for x, i in enumerate(place) for y, j in enumerate(i) if j=='P']
    len_p = len(p_place)
    for i in range(len_p):
        for j in range(1+i, len_p):
            x1, y1 = p_place[i]
            x2, y2 = p_place[j]
            x_abs = abs(x1-x2)
            y_abs = abs(y1-y2)
            if x_abs + y_abs <= 2:
                x_min = min(x1,x2)
                y_min = min(y1,y2)
                between = [[i, j] for i in range(x_min, x_min+x_abs+1) for j in range(y_min, y_min+y_abs+1)]
                if len(between) == 2:
                    return 0
                for b in between:
                    if place[b[0]][b[1]] == 'O':
                        return 0
    return 1