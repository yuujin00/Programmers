import math

def solution(n):
    
    N=math.sqrt(n)
    if N%1==0 :
        return (N+1)**2
    else :
        return -1