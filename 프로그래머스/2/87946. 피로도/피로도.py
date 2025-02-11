from itertools import permutations

def solution(k, dungeons):
    answer = -1
    
    for per in permutations(dungeons):
            c_k=k
            cnt=0
            for i,j in per:
                if i <= c_k :
                    c_k-=j
                    cnt+=1
                else :
                    break
            answer=max(answer,cnt)
        
    return answer