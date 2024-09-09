# 보석 쇼핑

from collections import Counter

def solution(gems):
    answer = []
    gemCnt=len(set(gems))
    gemlist=Counter()
    start=0
    
    for end in range(len(gems)):
        gemlist[gems[end]]+=1
        #print(gemlist,len(gemlist),start,end)
        
        while len(gemlist) == gemCnt :
        #Counter({'DIA': 3, 'RUBY': 2, 'EMERALD': 1, 'SAPPHIRE': 1}) 4 0 6
            answer.append((start+1,end+1))
            gemlist[gems[start]]-=1
            #gems[0]='DIA' => 'DIA' : 3-1 = 2
            
            if gemlist[gems[start]] == 0:
                # 'RUBY' : 0
                del gemlist[gems[start]]
                #print(gemlist,len(gemlist),start,end)
                #Counter({'DIA': 2, 'EMERALD': 1, 'SAPPHIRE': 1}) 3 2 6
            
            start+=1
            #print(answer, start)
    answer.sort(key=lambda x: (x[1]-x[0]))
    return answer[0]