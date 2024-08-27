def solution(array, commands):
    answer = []
    
    for command in commands :
        tmp=array
        tmp=sorted(tmp[command[0]-1:command[1]])
        answer.append(tmp[(command[2]-1)])
    
    return answer