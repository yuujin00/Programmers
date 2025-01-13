A,B,C =map(int,input().split())

def sol(n): 
    if n==1:
        return A % C

    n_half=sol(n//2)

    if n%2==0 :
        return n_half * n_half % C
    else :
        return (n_half * n_half * A) % C

print(sol(B))