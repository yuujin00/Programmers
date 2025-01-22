from itertools import combinations

L, C=map(int,input().split(' '))
Clist=sorted(list(input().split(' ')))

# 최소 한 개의 모음(a, e, i, o, u)과 최소 두 개의 자음

# 모음
mo=['a','e','i','o','u']
# 자음
ja=[i for i in 'bcdfghjklmnpqrstvwxyz']


for lock in list(combinations(Clist,L)):
    mo_cnt=0
    ja_cnt=0

    for i in lock:
        if i in mo:
            mo_cnt+=1
        if i in ja:
            ja_cnt+=1

    if mo_cnt>=1 and ja_cnt>=2:
        print(''.join(lock))