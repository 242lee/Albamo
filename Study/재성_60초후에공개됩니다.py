def solution(play_time, adv_time, logs):
    ''' 
    광고효과를 높이기 위해 시청자들이 가장 많이 보는 구간에 공익광고를 넣으려고 합니다. 
    동영상 재생시간 길이 play_time,  
    공익광고의 재생시간 길이 adv_time,  
    시청자들이 해당 동영상을 재생했던 구간 정보 logs 
    
    output:
    시청자들의 누적 재생시간이 가장 많이 나오는 곳에 공익광고를 삽입합니다.
    공익광고가 들어갈 시작 시각을 구해서 return 합니다.
    여러 곳이라면, 그 중에서 가장 빠른 시작 시각을 return 합니다.
    HH:MM:SS 형식의 8자리 문자열로 반환합니다.
    '''

    # HH:MM:SS 형식의 시간을 초(sec) 단위로 변환하는 함수
    def str_to_sec(time_str):
        h, m, s = map(int, time_str.split(':'))
        return h * 3600 + m * 60 + s  # 초로 변환하여 반환

    # 초 단위 시간을 HH:MM:SS 형식으로 변환하는 함수
    def sec_to_str(seconds):
        h = str(seconds // 3600).zfill(2)  # 시간 계산 (3600초 = 1시간)
        m = str((seconds % 3600) // 60).zfill(2)  # 분 계산 (60초 = 1분)
        s = str(seconds % 60).zfill(2)  # 초 계산
        return f'{h}:{m}:{s}'  # HH:MM:SS 형식으로 반환
    
    # 동영상 전체 재생 시간과 광고 시간(초 단위로 변환)
    play_sec = str_to_sec(play_time)
    adv_sec = str_to_sec(adv_time)
    
    # 시청자들의 로그를 바탕으로 시청 변화량을 기록할 타임라인 배열 생성
    # play_sec + 1 크기의 배열을 생성하여 초 단위로 시청자 수를 추적
    timeline = [0] * (play_sec + 1)
    
    # 각 시청 로그의 시작 시간에는 시청자 수 증가, 종료 시간에는 감소
    for log in logs:
        start, end = map(str_to_sec, log.split('-'))  # 각 로그를 시작과 종료 시간으로 분리
        timeline[start] += 1  # 시작 시간에 시청자 증가
        timeline[end] -= 1  # 종료 시간에 시청자 감소
    
    # 시간에 따른 시청자 수 변화를 누적하여 총 시청자 수 계산
    for i in range(1, play_sec):
        timeline[i] += timeline[i-1]  # 이전 시간의 시청자 수를 더함 (구간별 시청자 누적)
    
    # 시간에 따른 누적 시청 시간을 계산 (시청자 수를 계속 누적하여 더해나감)
    for i in range(1, play_sec):
        timeline[i] += timeline[i-1]  # 이전 시간까지의 누적 시청 시간
    
    # 광고가 들어갈 수 있는 구간 중 누적 시청 시간이 가장 많은 구간을 찾음
    # 첫 번째 광고 구간의 누적 시청 시간 (0초 ~ 광고 시간)
    max_view = timeline[adv_sec-1]  # 첫 번째 광고 구간의 시청자 수
    max_time = 0  # 광고를 시작할 최적의 시간을 기록할 변수
    
    # 광고를 시작할 수 있는 모든 구간을 탐색 (광고가 끝나는 시간이 전체 재생시간을 넘지 않는 범위)
    for i in range(adv_sec, play_sec):
        curr_view = timeline[i] - timeline[i-adv_sec]  # 현재 구간의 누적 시청 시간 계산
        if curr_view > max_view:  # 현재 구간의 누적 시청 시간이 최대일 경우
            max_view = curr_view  # 최대 시청 시간을 갱신
            max_time = i - adv_sec + 1  # 광고 시작 시간을 갱신
    
    # 최종적으로 계산된 최적의 광고 시작 시간을 HH:MM:SS 형식으로 반환
    return sec_to_str(max_time)
