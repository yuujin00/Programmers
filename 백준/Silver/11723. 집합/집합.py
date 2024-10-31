import sys
input = sys.stdin.readline

n=int(input())

S=set()
while n>0 :
    word=list(input().split())
    if word[0]=='add' :
        S.add(int(word[1]))
    elif word[0]=='check' :
        if int(word[1]) in S :
            print(1)
        else :
            print(0)
    elif word[0]=='remove' :
        try:
          S.remove(int(word[1]))
        except:
          pass
    elif word[0]=='toggle' :
        if int(word[1]) in S :
            S.remove(int(word[1]))
        else :
            S.add(int(word[1]))
    elif word[0]=='all' :
        S={1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20}
    else :
        S=set()
    n-=1