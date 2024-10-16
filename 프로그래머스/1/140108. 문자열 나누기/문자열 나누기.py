def solution(s):
    answer = 0
    str=''
    p,r=0,0
    for i in s :
        if str=='':
            str+=i
            p+=1
            continue
            
        if str==i :
            p+=1
        else : 
            r+=1
        
        if(p==r) :
            answer+=1
            p,r=0,0
            str=''
    
    if p!=0 : answer+=1
    return answer