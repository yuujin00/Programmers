def solution(arr):
    answer = []
    for i in arr:
        if i not in answer[-1:]:
            answer.append(i)
    return answer