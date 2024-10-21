def solution(target):
    # DP 배열 초기화: [최소 다트 수, 싱글/불 개수]
    dp = [[float('inf'), 0] for _ in range(target + 1)]
    dp[0] = [0, 0]  # 0점은 다트 던짐 없이 만들 수 있음

    # 다트로 얻을 수 있는 모든 점수 리스트 구성
    scores = set([50])  # 불점
    for i in range(1, 21):
        scores.add(i)      # 싱글
        scores.add(i * 2)  # 더블
        scores.add(i * 3)  # 트리플

    # DP로 점수 만들기
    for score in range(1, target + 1):
        for s in scores:
            if score >= s:
                prev_darts, prev_singles = dp[score - s]
                current_darts = prev_darts + 1
                current_singles = prev_singles + (1 if s <= 20 or s == 50 else 0)  # 싱글 또는 불을 맞췄을 경우
                
                # 최소 다트 수를 갱신하거나 다트 수가 같을 때 싱글/불 개수가 더 많은 경우
                if current_darts < dp[score][0] or (current_darts == dp[score][0] and current_singles > dp[score][1]):
                    dp[score] = [current_darts, current_singles]

    return dp[target]
