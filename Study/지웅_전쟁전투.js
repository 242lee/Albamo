// const input = require('fs').readFileSync('/dev/stdin').toString().split(' ');
let input = require('fs').readFileSync('./input.txt').toString().trim().split('\n');

// 전쟁 - 전투
// 위력의 정의 : N명이 뭉쳐있을 때, N**2 (대각 인접은 인접이 아님, 오로지 십자)
const NM = input.splice(0,1)
const [M, N] = NM[0].split(' ').map((numb) => Number(numb));
let matrix = []
for (let i = 0; i < N; i ++) {
    matrix.push(input[i].split(''))
}

let WPower = 0;
let BPower = 0;

// node로 queue 구현 어려우니 가라로 일단 구현해보자.
// 4방향 정의
const di = [0,0,1,-1]
const dj = [1,-1,0,0]

function bfs(si, sj) {
    let qI = [];
    let qJ = [];
    let count = 0;
    const pivot = matrix[si][sj];
    qI.push(si)
    qJ.push(sj)
    count ++
    matrix[si][sj] = count
    while (qI.length > 0) {
        const nI = qI.splice(0,1)[0]
        const nJ = qJ.splice(0,1)[0]
        for (let dir = 0; dir < 4; dir ++) {
            var nextI = nI + di[dir]
            var nextJ = nJ + dj[dir]
            if (0<=nextI && nextI < N && 0<=nextJ && nextJ<M && matrix[nextI][nextJ] === pivot) {
                // console.log('matrix value',matrix[nextI][nextJ], nextI, nextJ)
                qI.push(nextI)
                qJ.push(nextJ)
                count ++
                matrix[nextI][nextJ] = count
            }
        }
    }
    return count;
}

for (let i = 0; i < N; i ++) {
    for (let j = 0; j < M; j ++) {
        if (matrix[i][j] === 'W' || matrix[i][j] === 'B') {
            const teamColor = matrix[i][j];
            const power = bfs(i,j);
            // console.log(power)
            if (teamColor === 'W') {
                WPower += power**2
            } else {
                BPower += power**2
            }
        }
    }
}
console.log(WPower, BPower);
