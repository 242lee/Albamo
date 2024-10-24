# 시분초로 주어진 것을 모두 초로 바꿈
# 시작점에 1, 끝점에 -1을 마킹
# 누적합을 구해
def convert(time):
    h, m, s = time.split(':')
    return int(h) * 60 ** 2 + int(m) * 60 + int(s)

def solution(play_time, adv_time, logs):
    playSec = convert(play_time)
    advSec = convert(adv_time)

    totalSec = [0 for _ in range(playSec + 1)]
    for log in logs:
        start, end = log.split('-')
        startSec = convert(start)
        endSec = convert(end)
        
        totalSec[startSec] += 1                 # 시작과 끝을 마킹 (시작은 1, 끝은 -1)
        totalSec[endSec] -= 1

    for i in range(1, playSec + 1):
        totalSec[i] += totalSec[i - 1]          # 누적으로 더해서 시청자 수 구하기

    tmpSum = sum(totalSec[:advSec])
    maxSum = tmpSum
    maxIdx = 0

    for j in range(advSec, playSec):            # 기존 합에서 맨 앞 숫자 빼고, 다음 숫자 더하기
        tmpSum = tmpSum - totalSec[j - advSec] + totalSec[j]
        if maxSum < tmpSum:
            maxSum = tmpSum
            maxIdx = j + 1 - advSec             # 광고 시작 위치 totalSec[j - advSec]의 바로 오른쪽

    ansH = maxIdx // 60**2  # 시
    ansM = (maxIdx // 60) % 60  # 분
    ansS = maxIdx % 60  # 초
    answer = '%02d:%02d:%02d' % (ansH, ansM, ansS) # 시:분:초로 포맷

    return answer