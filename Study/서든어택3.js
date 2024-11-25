// const input = require('fs').readFileSync('/dev/stdin').toString().split(' ');
let input = require('fs').readFileSync('./input.txt').toString().trim().split('\n');
const N = Number(input[0])
const players = input[1].split(' ').map((number) => Number(number))
// players[0]이 준원이의 공격력임
// 준원이 자신보다 공격력 낮은 플레이어들을 먹고 왕이 될 수 있냐 봐야함.
let mainPlayer = players.splice(0,1)[0]
players.sort((a, b) => a - b)

let answer = 'Yes'
for (const player of players) {
    console.log(mainPlayer)
    if (mainPlayer > player) {
        mainPlayer = mainPlayer + player
    } else {
        answer = 'No'
        break;
    }
}
console.log(answer)
