def solution(arr):
    answer = []
    
    for num in arr :
        if num not in answer[-1:]:
            answer.append(num)
    return answer

