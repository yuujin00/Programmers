def solution(d, budget):
    answer,cnt = 0,0
    d.sort()
    
    for i in d:
        cnt+=i
        if cnt==budget:
            answer+=1
            break
        elif cnt<budget :
            answer+=1
        else :
            cnt-=i
    return answer