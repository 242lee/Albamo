def solution(diffs, times, limit):
    def is_valid(level):
        total_time = 0
        time_prev = 0
        
        for diff, time_cur in zip(diffs, times):
            if diff <= level:
                total_time += time_cur
            else:
                mistakes = diff - level
                total_time += mistakes * (time_cur + time_prev) + time_cur
            
            if total_time > limit:
                return False
            
            time_prev = time_cur
        
        return total_time <= limit

    # 이분 탐색 범위
    left, right = 1, max(diffs)
    answer = right

    while left <= right:
        mid = (left + right) // 2
        if is_valid(mid):
            answer = mid
            right = mid - 1
        else:
            left = mid + 1

    return answer
