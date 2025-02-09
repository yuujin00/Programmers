S = input()
S_counter=dict()

for s in S:
    if s not in S_counter :
        S_counter[s]= 1
    else :
        S_counter[s]+=1

def lucky(string, counter, c_1):
    global cnt
    if len(string)==len(S):
        cnt+=1
        return 
    
    for c in counter:
        if counter[c] > 0 and c!= c_1 :
            counter[c] -=1
            lucky(string+c,counter,c)
            # 이전으로 되돌리기
            counter[c] +=1

cnt=0
lucky('',S_counter,'')
print(cnt)
