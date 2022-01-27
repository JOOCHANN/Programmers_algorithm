# K번째 수
# 정렬
# 2022.01.27
# 19:25 ~ 20:10 (45 min)
# 후기 : 세명의 사람이 찍는 순서의 규칙을 찾아 리스트로 사전에 만들어주느라 시간이 소요됨.
#       찍는 순서의 패턴을 반복되는 위치까지만 미리 리스트로 만들어두고, 
#       각기 다른 순환주기마다 순서대로 불러왔으면 더 쉬웠을듯함.

def solution(answers):
    answer = []
    a = len(answers)
    num_1 = [i%5+1 for i in range(a)]
    n_2 = [1, 3, 4, 5]
    num_2 = [2 if i%2==0 else n_2[(i//2)%4] for i in range(a)]
    n_3 = [3, 1, 2, 4, 5]
    num_3 = [n_3[(i//2)%5] if (i%2==0 and i>0) else n_3[(i//2)%5] for i in range(a)]
    
    tmp = [sum([1 for n, an in zip(num_1, answers) if n == an]), 
           sum([1 for n, an in zip(num_2, answers) if n == an]),
           sum([1 for n, an in zip(num_3, answers) if n == an])]
    
    maxx = max(tmp)
    for _, t in enumerate(tmp):
        if maxx == t:
            answer.append(_+1)

    return answer