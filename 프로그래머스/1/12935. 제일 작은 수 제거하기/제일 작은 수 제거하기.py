def solution(arr):
    answer = []
    
    if len(arr)==1 : 
        answer.append(-1)
    else :
        arr.remove(min(arr))
        return arr
    return answer