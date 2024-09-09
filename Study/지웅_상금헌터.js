const input = require('fs').readFileSync("../input.txt").toString().split('\n');
// const input = require('fs').readFileSync("/dev/stdin").toString().split('\n');

for (let i = 1; i < input.length; i++) {
    input[i] = input[i].split(' ').map(Number)
}
input[0] = parseInt(input[0]);

function first(score, a) {
    if (score > 21 || score === 0) {
        return 0
    } else if (score === 1) {
        return 5000000
    } else if (score <= 3) {
        return 3000000
    } else if (score <= 6) {
        return 2000000
    } else if (score <= 10) {
        return 500000
    } else if (score <= 15) {
        return 300000
    } else if (score <= 21) {
        return 100000
    }
}

function second(score, b) {
    if (score > 31 || score === 0) {
        return 0
    } else if (score === 1) {
        return 5120000
    } else if (score <= 3) {
        return 2560000
    } else if (score <= 7) {
        return 1280000
    } else if (score <= 15) {
        return 640000
    } else if (score <= 31) {
        return 320000
    }
}

for (let k = 1; k < input[0] + 1; k++) {
    var first_input = input[k][0];
    var second_input = input[k][1];
    if (first_input > 100) {
        first_input = 0
    }
    if (second_input > 64) {
        second_input = 0
    }

    var first_prize = first(first_input)
    var second_prize = second(second_input)

    console.log(first_prize + second_prize);
}
