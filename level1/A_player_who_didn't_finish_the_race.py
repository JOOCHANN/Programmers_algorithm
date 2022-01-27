# 완주하지 못한 선수
# 해시
# 2022.01.27
# 16:25 ~ 16:50 (25 min)
# 후기 : 효율성 테스트에서 시간초과가 안뜨도록 하기 위해 시간이 다소 소요됨.
#       다른사람이 푼 방식을 보니 collections 라이버리의 counter를 사용하여 
#       리스트에 존재하는 요소들의 수를 세어주고 두 딕셔너리를 (-)를 통해 비교 하였음. 
#       collections 라이버리의 counter와 딕셔너리를 (-)를 통하여 비교할 수 있는것을 배움.

def solution(participant, completion):
    participant.sort()
    completion.sort()
    
    for p, c in zip(participant, completion+['']):
        if p != c:
            return p