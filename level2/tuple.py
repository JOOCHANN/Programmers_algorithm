# 튜플
# 2019 카카오 개발자 겨울 인턴십
# 2022.02.17
# 13:00 ~ 13:17 (17 min)
# 후기 : 낮은 길이의 숫자부터 불러와 answer에 넣으면 쉽게 풀 수 있음.

def solution(s):
    answer = []
    s = "".join(s.split("}")[:-2]).split("{")[2:]
    len_s = sorted([[len(i), _] for _, i in enumerate(s)])
    for (i, _) in len_s:
        tmp = s[_].split(",")
        for t in tmp:
            if t :
                t = int(t)
                if t not in answer:
                    answer.append(t)

    return answer