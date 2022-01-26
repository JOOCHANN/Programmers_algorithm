# 오픈채팅방 
# 2019 KAKAO BLIND RECRUITMENT
# 2022.01.26
# 15:40 ~ 16:05 (35 min)
# 후기 : 큰 어려움 없었다. 굳이 uid_set이 없이 바로 dictionary를 만들었어도 됐을것 같다.

def solution(record):
    answer = []
    record_action = ["Enter", "Leave", "Change"]
    result_action = ["님이 들어왔습니다.", "님이 나갔습니다."]
    uid_set = set(s.split(" ")[1] for s in record)
    dic = {uid:"" for uid in uid_set}
    
    for s in record:
        r = s.split(" ")
        
        if r[0] == record_action[0]: # Enter
            dic[r[1]] = r[2]
        elif r[0] == record_action[2]: # Change
            dic[r[1]] = r[2]
    
    for s in record:
        r = s.split(" ")
        
        if r[0] == record_action[0]: # Enter
            answer.append(dic[r[1]] + result_action[0])
        elif r[0] == record_action[1]: # Leave
            answer.append(dic[r[1]] + result_action[1])

    
    return answer