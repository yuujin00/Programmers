def solution(k, tangerine):
    answer = 0
    
    cnt={}
    
    for i in tangerine :
        if i in cnt :
            cnt[i]+=1
        else :
            cnt[i]=1
            
    cnt=sorted(cnt.items(), key=lambda x : x[1])

    while k>0 :
        k-=cnt.pop()[1]
        answer+=1
    return answer