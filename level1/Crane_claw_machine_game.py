# 크레인 인형뽑기 게임
# 2019 카카오 개발자 겨울 인턴
# 2022.01.26
# 17:05 ~ 17:35 (30 min)
# 후기 : 크게 어렵지 않았으며 board.T 리스트를 새로 만들때 filter를 이용하여 0을 모두 지워버렸으면, 
#       2중 반복문을 사용하지 않고 훨신 더 간략했을듯함.
#       ex) board = list(map(lambda x: list(filter(lambda y: y > 0, x)), zip(*board)))

def solution(board, moves):
    answer = 0
    cup = []
    board = [list(x) for x in zip(*board)]
    
    for _, m in enumerate(moves):
        for __, b in enumerate(board[m-1]):
            if b != 0:
                cup.append(board[m-1][__])
                board[m-1][__] = 0
                break
            else:
                continue
        
        if len(cup) > 1 :
            if cup[-1] == cup[-2]:
                cup = cup[:-2]
                answer += 2

    return answer