# 행렬 테두리 회전하기
# 2021 Dev-Matching: 웹 백엔드 개발
# 2022.02.04
# 15:20 ~ 16:20 (60 min)
# 후기 : list에서 2차원 배열 슬라이싱을 하려면 for문을 필연적으로 써야하기 때문에 numpy를 사용함.
#       numpy를 사용하면 for문없이도 연산 가능함. 
#       핵심 아이디어는 회전할 번호들을 stack 리스트에 저장하고 이를 rotation 시킨 후에 
#       원본 grid 에다가 빼내온 순서대로 다시 저장을 하는 방법임.


import numpy as np

def solution(rows, columns, queries):
    answer = []
    grid = np.array([[c+1+r*columns for c in range(columns)]for r in range(rows)])
    stack = []
    for q in queries:
        x1, y1 = q[0]-1, q[1]-1
        x2, y2 = q[2]-1, q[3]-1
        
        stack = list(grid[x1, y1:y2+1]) + list(grid[x1+1:x2, y2]) + \
                list(grid[x2, y1:y2+1][::-1]) + list(grid[x1+1:x2, y1][::-1]) 
        last = stack.pop()
        stack = [last] + stack
        
        grid[x1, y1:y2+1] = stack[:(y2+1-y1)]
        grid[x1+1:x2, y2] = stack[(y2+1-y1):(y2+1-y1)+(x2-1-x1)]
        grid[x2, y1:y2+1] = stack[(y2+1-y1)+(x2-1-x1):(y2+1-y1)*2+(x2-1-x1)][::-1]
        grid[x1+1:x2, y1] = stack[(y2+1-y1)*2+(x2-1-x1):(y2+1-y1)*2+(x2-1-x1)*2][::-1]

        answer.append(int(min(stack)))
    
    return answer