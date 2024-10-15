def solution(name, yearning, photo):
    answer = []
    dic={}
    
    for i in range(len(name)) :
        dic[name[i]]=yearning[i]
        
    for photo_ in photo:
        tmp=0
        for i in photo_ :
            if i in dic : 
                tmp+=dic[i]
        answer.append(tmp)
    
    return answer