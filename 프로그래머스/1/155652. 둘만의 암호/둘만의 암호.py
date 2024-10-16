def solution(s, skip, index):
    answer = ''
    aph=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    for i in skip :
        aph.remove(i)
        
    for i in s:
        a="".join(aph)
        answer+=aph[(a.find(i)+index)%(26-len(skip))]
    return answer