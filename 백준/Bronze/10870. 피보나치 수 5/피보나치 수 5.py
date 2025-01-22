def f(N):
    if N==1 :
        return 1
    elif N==0 :
        return 0

    return f(N-1)+f(N-2)

print(f(int(input())))