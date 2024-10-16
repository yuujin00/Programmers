def solution(lottos, win_nums):
    answer = []
    cnt=0
    
    rank=[6,6,5,4,3,2,1]
    
    for i in lottos :
        if i in win_nums :
            cnt+=1
    
    return rank[lottos.count(0) + cnt],rank[cnt]