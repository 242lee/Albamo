def solution(diffs, times, limit):
    def can_solve_with_level(level):
        # 숙련도가 level일 때 제한 시간 내에 모든 퍼즐을 해결할 수 있는지 확인.
        total_time = 0
        time_prev = 0  # 이전 퍼즐의 소요 시간

        for i in range(len(diffs)):
            diff = diffs[i]
            time_cur = times[i]
            if diff <= level:
                total_time += time_cur
            else:
                # 퍼즐을 diff - level번 틀림
                mistakes = diff - level
                total_time += mistakes * (time_cur + time_prev) + time_cur
            time_prev = time_cur  # 현재 퍼즐의 시간을 이전 퍼즐 시간으로 갱신

            # 제한 시간을 초과하면 False
            if total_time > limit:
                return False
        return True

    # 이분 탐색으로 숙련도의 최솟값을 찾음
    left, right = 1, max(diffs)
    answer = right

    while left <= right:
        mid = (left + right) // 2
        if can_solve_with_level(mid):
            answer = mid
            right = mid - 1
        else:
            left = mid + 1

    return answer
