# 가장 먼 노드
# 그래프
# 2022.02.03
# 18:30 ~ 20:05 (95 min)
# 후기 : 노드 수만큼 방문 리스트를 생성하고 큐를 만들어 줄때, 
#       방문할 노드와 방문 횟수를 기록할 count를 합쳐서 생성해 주는것이 핵심

from collections import deque

def solution(n, edge):
    visited = [0]*n
    num = [set() for i in range(n)]
    for (e1, e2) in edge:
        num[e1-1].add(e2-1)
        num[e2-1].add(e1-1)
    
    visited = BFS(0, visited, num)
    
    return visited.count(max(visited))

def BFS(v, visited, num):
    count = 0
    q = deque([[v, count]])
    while q :
        value = q.popleft()
        v = value[0]
        count = value[1]
        if visited[v] == 0:
            count += 1
            visited[v] = count
            for i in num[v]:
                if visited[i] == 0:
                    q.append([i, count]) 
    return visited