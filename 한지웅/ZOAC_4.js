const input = require('fs').readFileSync("input.txt").toString().trim().split(" ");
// const input = require('fs').readFileSync("/dev/stdin").toString().trim().split(" ");

function main(input_array) {

    H = Number(input_array[0]);
    W = Number(input_array[1]);
    N = Number(input_array[2]);
    M = Number(input_array[3]);
//     size : 행 H, 열 W
//     띄어앉기 행 : N, 열: M
//     0,0자리엔 인원 고정
    let row = 0
    let col = 0
    // row
    for (let i = 1; i <= H; i = i + N + 1) {
        col ++
    }
    for (let i = 1; i <= W; i = i + M + 1) {
        row ++
    }
    console.log(row * col)
}

main(input)
// main("5 4 1 1")
