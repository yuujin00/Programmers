N=1000-int(input())
cnt=0

# 500엔, 100엔, 50엔, 10엔, 5엔, 1엔
cnt += N//500
N %= 500

cnt += N//100
N %= 100

cnt += N//50
N %= 50

cnt += N//10
N %= 10

cnt += N//5
N %= 5

cnt += N//1
N %= 1

print(cnt)