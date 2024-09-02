// const input = require('fs').readFileSync("../input.txt").toString();
const input = require('fs').readFileSync("/dev/stdin").toString();

// data 첫번째는 계단의 step 수, 그 이후부터는 점수를 의미합니다.
const data = input.split('\n').map(Number);
const steps = data[0];
const scores = data.slice(1, data.length);
scores.unshift(0);

// dfs => 시간초과, DP활용
const dp = new Array(steps + 1).fill(0);

dp[1] = scores[1];
dp[2] = Math.max(scores[1] + scores[2], scores[2]);
dp[3] = Math.max(scores[1] + scores[3], scores[2] + scores[3]);
for (let j = 4; j < data.length; j++) {
    dp[j] = Math.max(scores[j-1] + dp[j-3], dp[j-2])
    dp[j] = dp[j] + scores[j]
}
console.log(dp[steps])
