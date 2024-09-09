const input = require('fs').readFileSync("../input.txt").toString().split('\n');
// const input = require('fs').readFileSync("/dev/stdin").toString().split('\n');

let data;
let N;
let M;
let K;
let virus_list;
let log_list;
let log_map;

data = input[0].split(' ').map(Number)
N = data[0]
M = data[1]
K = data[2]
virus_list = input[1].split(' ').map(Number)
log_list = input.slice(2,2 + M).map((data) => data.trim().split(' ').map(Number))
log_map = new Map()

for (virus_computer of virus_list) {
    log_map.set(virus_computer, null)
    // computer 번호, [가장 처음 로그를 보낸 시간, [보낸 컴퓨터 목록], 후보가 될 수 있는지]
}
// 1. 여기까지가 과정을 진행하기 위한 초기 셋팅

// 2. log_map에 시간순으로 setting 하기 시작한다.
for (log_data of log_list) {
    const log_time = log_data[0];
    const log_start = log_data[1];
    const log_end = log_data[2];

    const check_start = log_map.has(log_start);
    const check_end = log_map.has(log_end);


    if (check_start === true && check_end === false) {
        // 바이러스에 감영된 컴퓨터가 엉뚱한 컴퓨터에 보낸다?
        log_map.delete(log_start);
    }

    else if (check_start === true && check_end === true) {
        // 바이러스 => 바이러스라면 후보가 될 수 있음.

        // case 1. 처음 로그 보낸 경우
        if (log_map.get(log_start) === null) {
            const create_set = new Set()
            log_map.set(log_start, [log_time, create_set.add(log_end)]);

        }
        // case 2. 로그를 이전에 보낸 기록이 있음.
        if (log_map.get(log_start) !== null) {
            const time_history = log_map.get(log_start)[0]
            const log_history = log_map.get(log_start)[1]
            log_map.set(log_start, [time_history, log_history.add(log_end)])
        }
    }
}

const log_map_array = Array.from(log_map)
log_map_array.sort((a,b) => {
    if (a[1] === null) return 1;
    if (b[1] === null) return -1;
    return a[1][0] - b [1][0]
})
console.log(log_map_array)

function dfs(s) {
    let current = s;
    let stack = [current]
    while (stack.length > 0) {
        const future = log_map.get(current);
        console.log(future)
        break
    }
}

for (k of log_map_array) {
    if (k[1] !== null) {
        const start_k = k[0];
        const time_k = k[1][0];
        const end_k = Array.from(k[1][1]);
        console.log(start_k, time_k, end_k);
        dfs(start_k)
    }
}
