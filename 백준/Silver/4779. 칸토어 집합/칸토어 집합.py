def Cantor(N):
    if N == 1:
        return '-'
        
    left = Cantor(N // 3)
    center = ' ' * (N // 3)
    
    return left + center + left

while True:
    try:
        n = int(input())
        N = 3 ** n
        print(Cantor(N))
    except :
        break
