// const input = require('fs').readFileSync('/dev/stdin').toString().split(' ');
let input = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');

const nwL = input[0].split(' ').map((number) => (Number(number)))
const n = nwL[0]
const w = nwL[1]
const L = nwL[2]

const truck = input[1].split(' ').map((number) => Number(number))

// bridege 를 mapping (초기는 다리의 길이만큼 빈 값 할당)
const bridgeMap = new Map();
for (let i = 0; i < w; i++) {
    bridgeMap.set(i,0)
}
// console.log(bridgeMap)
// 시간을 보내며 map의 무게를 변경시킨다.
// 그와 동시에 weight 변수를 따로 관리하며 복잡도를 줄인다.
let weight = 0
let truckIndex = 0
let ans = 0
//
while (true) {
    // 마지막 항목의 트럭을 빼야함.
    weight = weight - bridgeMap.get(w-1)
    bridgeMap.set(w-1, 0)

    // 마지막 빼고 나머지 이동 과정 진행
    for (let j = w-1; j > 0; j--) {
        bridgeMap.set(j, bridgeMap.get(j-1))
        bridgeMap.set(j-1, 0)
    }

    // 트럭이 다리에 올라탈 수 있는지 확인
    if (truckIndex < n && bridgeMap.get(0) === 0 && weight + truck[truckIndex] <= L) {
        bridgeMap.set(0, truck[truckIndex])
        weight += truck[truckIndex]
        truckIndex ++
    }

    // console.log(bridgeMap, truckIndex)
    ans ++
    if (truckIndex >= n && weight === 0) {
        console.log(ans)
        return
    }
}
