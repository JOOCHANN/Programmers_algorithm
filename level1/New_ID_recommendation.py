# 신규 아이디 추천
# 2021 KAKAO BLIND RECRUITMENT
# 2022.01.25
# 15:30 ~ 16:00 (30 min)
# 후기 : 정규식으로 풀면 간단하다고 하지만, 외워야 할 것이 많아 일반적인 이러한 방식도 괜찮은거 같음.
#       중복된 '.'를 하나의 '.'으로 변경하는 부분을 반복문으로 replace('..')을 사용하여 푸는 것이 더 정확하지만,
#       양 끝에 있는 '.'을 제거하는 부분이 바로 뒷 부분이므로 아래와 같이 해줘도 오답은 아니라고 생각함.

def solution(new_id):
    special = ['-', '_', '.']
    answer = ''
    new_id = new_id.lower()
    new_id = ''.join(c for c in new_id if c.isalnum() or c in special)
    new_id = ''.join('.'+d for d in new_id.split('.') if d != '')
    new_id = new_id.strip('.')
    if not(new_id) : new_id = "a"
    new_id = new_id[:15]
    new_id = new_id.rstrip('.')
    if len(new_id) == 1:
        new_id = new_id + new_id[-1] + new_id[-1]
    if len(new_id) == 2:
        new_id = new_id + new_id[-1]
    
    answer = new_id
    return answer