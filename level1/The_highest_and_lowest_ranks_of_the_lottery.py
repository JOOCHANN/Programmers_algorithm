# 로또의 최고 순위와 최저 순위
# 2021 Dev-Matching: 웹 백엔드 개발
# 2022.01.25
# 15:00 ~ 15:13 (13 min)
# 후기 : 쓸데없이 all이라는 큰 배열을 생성한것 같음. 
#       if x in lottos 로 배열안에 정답이 있는지 찾으면 되는 부분이었음.
#       그리고, rank도 rank=[6,6,5,4,3,2,1]로 선언하였으면 더욱 간단했을듯

def solution(lottos, win_nums):

    answer = []
    num_zero = lottos.count(0)
    all = {i+1 : 0 for i in range(45)}
    rank = {6:1, 5:2, 4:3, 3:4, 2:5, 1:6, 0:6}
    count_0 = 0
    same_count = 0

    for k in win_nums:
        all[k] = 1

    for k in lottos:
        if k == 0 :
            count_0 += 1
        else:
            if all[k] == 1:
                same_count += 1

    answer.append(rank[count_0+same_count])
    answer.append(rank[same_count])
    return answer