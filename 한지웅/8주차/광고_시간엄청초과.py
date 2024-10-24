# 그냥 초 단위로 바꿔서 하나씩 세는 방식으로 진행함.
# 시간초과는 당연한 듯, 이 방식을 좀 바꿔야 할듯
def solution(play_time, adv_time, logs):
    play_time_list = list(map(int, play_time.split(":")))
    play_length = play_time_list[0] * 3600 + play_time_list[1] * 60 + play_time_list[2]
    matrix = [0 for _ in range(play_length)]

    adv_time_list = list(map(int, adv_time.split(":")))
    adv_length = adv_time_list[0] * 3600 + adv_time_list[1] * 60 + adv_time_list[2]

    for log in logs:
        start_log, end_log = log.split("-")
        start_log_list = list(map(int, start_log.split(":")))
        end_log_list = list(map(int, end_log.split(":")))
        start_log_time = start_log_list[0] * 3600 + start_log_list[1] * 60 + start_log_list[2]
        end_log_time = end_log_list[0] * 3600 + end_log_list[1] * 60 + end_log_list[2]
        for i in range(start_log_time, end_log_time):
            matrix[i] += 1

    mxValue = 0
    mxIndex = 0
    for j in range(play_length - adv_length):
        if sum(matrix[j:j + adv_length]) > mxValue:
            mxValue = sum(matrix[j:j + adv_length])
            mxIndex = j
            if mxValue == adv_length * len(logs):
                break

    answer = ''
    HOUR = int(mxIndex //3600)
    mxIndex -= HOUR * 3600
    MINUTE = int(mxIndex // 60)
    mxIndex -= MINUTE * 60

    HOUR = str(HOUR)
    MINUTE = str(MINUTE)
    SECOND = str(int(mxIndex))
    if len(HOUR) == 1:
        HOUR = '0' + HOUR
    if len(MINUTE) == 1:
        MINUTE = '0' + MINUTE
    if len(SECOND) == 1:
        SECOND = '0' + SECOND
    answer += HOUR + ':' + MINUTE + ':' + SECOND
    return answer

print(solution(play_time, adv_time, logs))
