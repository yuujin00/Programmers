def solution(video_len, pos, op_start, op_end, commands):
    # 시간을 초로 변환하는 함수
    def time_to_seconds(time_str):
        minutes, seconds = map(int, time_str.split(':'))
        return minutes * 60 + seconds

    # 초를 다시 mm:ss 형식으로 변환하는 함수
    def seconds_to_time(seconds):
        minutes = seconds // 60
        seconds = seconds % 60
        return f"{minutes:02}:{seconds:02}"

    # 입력값을 초로 변환
    current_time = time_to_seconds(pos)
    video_end = time_to_seconds(video_len)
    op_start_time = time_to_seconds(op_start)
    op_end_time = time_to_seconds(op_end)

    # 명령을 하나씩 처리
    for command in commands:
        # 오프닝 구간에 있는지 확인하고, 있으면 오프닝 끝으로 이동
        if op_start_time <= current_time <= op_end_time:
            current_time = op_end_time

        # 명령 처리
        if command == "next":
            current_time += 10
            if current_time > video_end:
                current_time = video_end
        elif command == "prev":
            current_time -= 10
            if current_time < 0:
                current_time = 0

        # 오프닝 구간에 다시 있는지 확인 후 이동
        if op_start_time <= current_time <= op_end_time:
            current_time = op_end_time

    # 최종 시간을 mm:ss 형식으로 변환하여 반환
    return seconds_to_time(current_time)
