# 네트워크
# 깊이/너비 우선 탐색(DFS/BFS)
# 2022.01.28
# 14:40 ~ ( min)
# 후기 : 재귀함수를 활용한 DFS 방식에 대해 연습할 수 있었음.
#       아직 DFS, BFS 방법이 익숙하지 않아서 좀더 연습을 해야될 것 같음.
#       방문하는 기록을 저장하는 visited를 만들고 한번에 연결되어 있는 모든 네트워크 들을 
#       반복적으로 탐색하여 끝나는 주기마다 answer에 1을 더해주는 방법임

def solution(n, computers):
    answer = 0
    visited = [0 for i in range(n)]
    for _ in range(n):
        if visited[_] == 0:
            DFS(n, computers, _, visited)
            answer += 1
            
    return answer

def DFS(n, computers, _, visited):
    visited[_] = 1
    for c in range(n):
        if c != _ and computers[_][c] == 1 and visited[c] == 0:
            DFS(n, computers, c, visited)
