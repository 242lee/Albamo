# 시간을 초로 변환하는 함수
def time_to_seconds(time_str):
    h, m, s = map(int, time_str.split(':'))
    return h * 3600 + m * 60 + s

# 초를 다시 시간 문자열로 변환하는 함수
def seconds_to_time(seconds):
    h = seconds // 3600
    m = (seconds % 3600) // 60
    s = seconds % 60
    return f'{h:02}:{m:02}:{s:02}'

def solution(play_time, adv_time, logs):
    # 전체 재생시간과 광고시간을 초로 변환
    play_seconds = time_to_seconds(play_time)
    adv_seconds = time_to_seconds(adv_time)

    # 각 시간의 시청자 변화를 기록하기 위한 리스트 (0초부터 play_time까지)
    viewers = [0] * (play_seconds + 1)

    # 각 로그를 파싱하여 시청 시작/종료 시간의 변화를 기록
    for log in logs:
        start, end = log.split('-')
        start_sec = time_to_seconds(start)
        end_sec = time_to_seconds(end)
        viewers[start_sec] += 1  # 시작점에서 시청자가 늘어남
        viewers[end_sec] -= 1    # 종료점에서 시청자가 줄어듦

    # 각 초에 실제 시청하고 있는 시청자 수를 계산 (변화 누적)
    for i in range(1, play_seconds + 1):
        viewers[i] += viewers[i - 1]

    # 각 초에 누적된 시청 시간 (0초부터 i초까지의 시청자 수 누적)
    for i in range(1, play_seconds + 1):
        viewers[i] += viewers[i - 1]

    # 가장 많은 누적 시청 시간을 가지는 광고 시작 시간 찾기
    max_view_time = 0
    max_start_time = 0

    # 광고가 시작될 수 있는 모든 시간을 탐색 (0초부터 play_time - adv_time까지)
    for start_time in range(play_seconds - adv_seconds + 1):
        end_time = start_time + adv_seconds

        # 누적 시청 시간 계산
        if start_time == 0:
            total_view_time = viewers[end_time - 1]
        else:
            total_view_time = viewers[end_time - 1] - viewers[start_time - 1]

        # 최대 누적 시청 시간을 가진 시작 시간을 갱신
        if total_view_time > max_view_time:
            max_view_time = total_view_time
            max_start_time = start_time

    # 초 단위로 구한 광고 시작 시간을 HH:MM:SS 형식으로 변환하여 반환
    return seconds_to_time(max_start_time)
