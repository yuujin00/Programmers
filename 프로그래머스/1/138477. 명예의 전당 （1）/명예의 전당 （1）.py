def solution(k, score):
    answer = []
    Round=[]
    
    for i in score:
        if len(Round)<k:
            Round.append(i)
        else :
            if min(Round)<i:
                Round.remove(min(Round))
                Round.append(i)
        answer.append(min(Round))
    
    return answer