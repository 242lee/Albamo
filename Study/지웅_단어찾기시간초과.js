/**
 * @param {character[][]} board
 * @param {string[]} words
 * @return {string[]}
 */

// 시작지점을 찾는 함수
var findStart = function(board, word, I, J) {
    const start = []
    for (let i = 0; i < I; i++) {
        for (let j = 0; j < J; j++) {
            if (board[i][j] === word[0]) {
                start.push([i,j])
            }
        }
    }
    return start
}

var chaseWord = function(si, sj, I, J, word, index, board, visited) {
    // 마지막 인덱스까지 도달했다면 단어를 찾은 것
    if (index === word.length) {
        return true
    }
    
    visited[si][sj] = true
    const di = [0,0,-1,1]
    const dj = [-1,1,0,0]
    
    // 인접한 4방향 탐색
    for (let dir = 0; dir < 4; dir++) {
        const nextI = si + di[dir]
        const nextJ = sj + dj[dir]
        
        // 다음 위치가 유효하고, 방문하지 않았고, 다음 글자와 일치하면 진행
        if (0 <= nextI && nextI < I && 
            0 <= nextJ && nextJ < J && 
            !visited[nextI][nextJ] && 
            board[nextI][nextJ] === word[index]) {
            
            // 다음 인덱스의 글자를 찾으러 이동
            if (chaseWord(nextI, nextJ, I, J, word, index + 1, board, visited)) {
                return true
            }
        }
    }
    
    // 현재 경로로는 단어를 못 찾았으므로 방문 표시를 제거하고 false 반환
    visited[si][sj] = false
    return false
}

var findWords = function(board, words) {
    const I = board.length
    const J = board[0].length
    const result = []
    
    for (let word of words) {
        const startCandidate = findStart(board, word, I, J)
        let found = false
        
        // 각 시작점에 대해 탐색
        for (let [i, j] of startCandidate) {
            // 방문 배열 초기화
            const visited = Array(I).fill().map(() => Array(J).fill(false))
            // 첫 글자부터 시작
            if (chaseWord(i, j, I, J, word, 1, board, visited)) {
                result.push(word)
                found = true
                break
            }
        }
    }
    
    return result
}
