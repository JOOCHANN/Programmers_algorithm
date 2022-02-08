# 수식 최대화
# 2020 카카오 인턴십
# 2022.02.08
# 16:05 ~ 16:40 (35 min)
# 후기 : list의 깊은 복사와 얕은 복사에 대해 알게됨.
#       eval()를 먼저 알고 있었더라면 while문안에 if 문을 쓸 필요가 없었음.


import copy

def solution(expression):
    answer = []
    operation = [['+', '-', '*'], ['+', '*', '-'], ['-', '+', '*'],\
                 ['-', '*', '+'], ['*', '+', '-'], ['*', '-', '+'],]
    tmp = ''
    ex = []
    for e in list(expression):
        if e.isdigit():
            tmp += e
        else:
            ex.append(tmp)
            ex.append(e)
            tmp = ''
    ex.append(tmp)
    
    for op in operation:
        result = copy.deepcopy(ex)
        for o in op:
            while o in result:
                a = int(result.pop(result.index(o)-1))
                b = int(result.pop(result.index(o)+1))
                o_index = result.index(o)
                if o == '+': result[o_index] = a+b
                elif o == '-': result[o_index] = a-b
                elif o == '*': result[o_index] = a*b
        answer.append(abs(result[0]))
    
    return max(answer)