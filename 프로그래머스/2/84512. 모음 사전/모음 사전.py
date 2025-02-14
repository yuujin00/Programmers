from itertools import product

def solution(word):
    words=[]
    for i in range(1,6):
        for dic in list(product("AEIOU",repeat=i)):
            words.append(''.join(dic))
    
    words.sort()
    
    return words.index(word)+1
    