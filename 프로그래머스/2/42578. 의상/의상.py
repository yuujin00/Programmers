def solution(clothes):
    answer = 1
    
    clothe_cnt={}
    
    for (i,j) in clothes :
        if j in clothe_cnt :
            clothe_cnt[j] += 1
        else :
            clothe_cnt[j] = 1
    
    print(clothe_cnt)
    
    for i in clothe_cnt :
        answer *= (clothe_cnt[i]+1)
        
    return answer-1