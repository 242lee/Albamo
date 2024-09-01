const input = require('fs').readFileSync("../input.txt").toString();
// const input = require('fs').readFileSync("/dev/stdin").toString();

const data= input.split('\n');
const target = data[0];
const block = data[1];

function search() {
    let idx = 0
    let result = 0
    while (idx + block.length <= target.length) {
        let pivot = target.slice(idx, idx + block.length);
        // console.log(pivot, block)
        if (pivot === block) {
            result ++
            idx = idx + block.length
        } else {
            idx ++
        }

    }
    console.log(result)
    return
}

search();
