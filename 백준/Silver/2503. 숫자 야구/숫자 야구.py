N = int(input())

# 서로 다른 숫자로 구성된 모든 세 자리수
all_cases = [f"{i}{j}{k}" for i in range(1, 10) for j in range(1, 10) for k in range(1, 10) if i != j and j != k and i != k]

# 스트라이크, 볼을 계산하는 함수
def count_strikes_balls(secret, guess):
    # 스트라이크: 숫자와 위치가 모두 일치
    strikes = sum(1 for x, y in zip(secret, guess) if x == y)
    # 볼: 숫자는 일치하지만 위치가 다름
    balls = len(set(secret) & set(guess)) - strikes
    return strikes, balls

for _ in range(N):
    num, s, b = input().split()
    num = str(num)
    s, b = int(s), int(b)

    # 스트라이크, 볼이 아닌 경우를 필터링
    new_cases = []
    for case in all_cases:
        # 스트라이크, 볼 계산
        calc_strikes, calc_balls = count_strikes_balls(case, num)
        # 스트라이크, 볼이 같은 경우만 추가
        if calc_strikes == s and calc_balls == b:
            new_cases.append(case)
    all_cases = new_cases

print(len(all_cases))