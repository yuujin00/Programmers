
N = int(input())

players = []
for _ in range(N):
    b_i, p_i, q_i, r_i = map(int, input().split())
    # 선수의 등번호, 세 순위의 곱, 세 순위의 합을 함께 저장
    players.append((b_i, p_i * q_i * r_i, p_i + q_i + r_i))

# 조건 곱/합/등번호 순서로 정렬렬
players.sort(key=lambda x: (x[1], x[2], x[0]))

print(players[0][0], players[1][0], players[2][0])