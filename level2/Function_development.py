# 기능개발
# 스택/큐
# 2022.01.27
# 17:35 ~ 18:05 (30 min)
# 후기 : 시간복잡도 면에서 고려가 부족한것 같음. 다른 사람들 코드를 보니 반복문 하나로도 충분히 풀수있었음.
#       모든 프로그레스를 동시에 진행한 상황을 보지말고, 맨 처음 프로그래스가 끝날때의 시간을 측정하여, 
#       이를 다음 번째에 이용했으면 반복문을 하나만 사용 할 수 있었음.

def solution(progresses, speeds):
    answer = []
    q = [[p, s, 0] for p, s in zip(progresses, speeds)]
    while q :
        for _, (p, s, b) in enumerate(q):
            if q[_][2] == 0:
                q[_][0] += s
            else:
                continue
            
            if q[_][0] >= 100:
                q[_][2] = 1
                
        idx = 0
        r = 0
        for _, (p, s, b) in enumerate(q):
            if _ == idx and q[_][2] == 1:
                r += 1
                idx += 1
            else:
                break
        
        if idx >= 1:
            answer.append(r)
            q = q[idx:]
        
    return answer