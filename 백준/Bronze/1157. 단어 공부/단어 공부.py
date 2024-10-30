word=input()

dic={}
k=[]

for w in word.upper() :
    if w in dic :
        dic[w]+=1
    else :
        dic[w]=1

m=max(dic.values())

for key, value in dic.items():
    if value == m :
        k.append(key)

if len(k)>1 :
    print('?')
else :
    print(k.pop())