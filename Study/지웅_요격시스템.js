// const targets = [[4,5],[4,8],[10,14],[11,13],[5,12],[3,7],[1,4]]
// 숫자 범위를 보니 완전 탐색으로 이를 해결하긴 쉽지 않다고 판단
// 그렇다면 하나 하나 입력을 받으며 계산을 진행할 수 있을까?

function solution(targets) {
    var answer = 1;
    // 우선 정렬한다.
    const sortedTargets = targets.sort((a,b) => a[0] - b[0]);
    // 이전 값을 비교하며, 요격을 할 때 새로운 요격 시스템이 필요한지 판단한다.
    let prev = sortedTargets[0]
    for (let i = 1; i < sortedTargets.length; i++) {
        // 이전 격추 범위와 현재 격추 범위가 겹치는 경우 prev 재설정
        // console.log(prev)
        if (sortedTargets[i][0] < prev[1]) {
            const a = sortedTargets[i][0]
            const b = prev[1] < sortedTargets[i][1] ? prev[1] : sortedTargets[i][1]
            // console.log(prev, sortedTargets[i], a, b)
            prev = [a,b]
        } else {
            prev = sortedTargets[i]
            answer ++
        }
    }
    // console.log(answer)
    return answer
}
// solution(targets)