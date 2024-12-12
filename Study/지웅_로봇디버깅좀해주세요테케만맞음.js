const points = [[3, 2], [6, 4], [4, 7], [1, 4]]
const routes = [[4, 2], [1, 3], [4, 2], [4, 3]]

// 구현방식
// 1. 초기 셋팅
// 2. 충돌확인 => 탈출확인 => 이동 ... 의 반복
// 단 충돌확인 이후 탈출 여부를 판단하기까지 진행.

function solution(points, routes) {
  var answer = 0;

  const routeLength = routes[0].length

  // P : point 정보 반영. Point 정보 갱신
  let P = new Map()
  for (point of Array.from(points.entries())) {
    P.set(point[0] + 1, point[1])
  }
  // R : robot의 현 위치 반영 (그리도 몇번째 경로를 목표로 가는지, 몇번째 목적지를 향해 가는지 또한 작성)
  let R = new Map()
  for (route of Array.from(routes.entries())) {
    R.set(route[0] + 1, [P.get(route[1][0]), P.get(route[1][1]), 2])
  }

  // console.log('P!', P)

  // 1. R을 보고 충돌 여부를 확인하는 함수 정의.
  function check(robotInfo) {
    const checkMap = new Map()
    for (info of robotInfo.entries()) {
      const coord = info[1][0][0].toString() + info[1][0][1].toString()
      if (checkMap.get(coord) === false) {
        // 이미 존재한다? 충돌 발생이므로
        checkMap.set(coord, true)
      } else if (checkMap.get(coord) === true){
        continue
      } else {
        checkMap.set(coord, false)
      }
    }
    // 작성한 checkMap으로 충돌을 카운트한다.
    let cnt = 0;
    for (res of checkMap.values()) {
      // console.log('res', res)
      if (res === true) {
        cnt ++
      }
    }
    return cnt
  }

  // 2. 이동하는 함수 정의
  function move(robotInfo) {
    // r이 최우선 이동임.
    const moveMap = new Map()
    for (info of robotInfo.entries()) {
      const current = info[1][0]
      const target = info[1][1]
      let next;
      if (current[0] !== target[0]) {
        next = current[0] > target[0] ? [current[0] - 1, current[1]] : [current[0] + 1, current[1]]
      } else {
        next = current[1] > target[1] ? [current[0], current[1] - 1] : [current[0], current[1] + 1]
      }

      // 만약 이동할 경로와 타겟이 동일한 경우 robotInfo자체를 또 수정해야함.
      if (next[0] === target[0] && next[1] === target[1]) {
        let nextTarget;
        if (P.get(info[1][2]) === routeLength) {
          nextTarget = false
          moveMap.set(info[0], [next, nextTarget, info[1][2] + 1])
        } else {
          nextTarget = P.get(routes[info[0]-1][info[1][2] + 2])
          moveMap.set(info[0], [next, nextTarget, info[1][2] + 1])
        }
      } else {
        moveMap.set(info[0], [next, target, info[1][2]])
      }
    }
    return moveMap
  }

  // 3. 탈출을 확인하는 함수 정의
  function escape(robotInfo) {
    const res = robotInfo
    for (info of robotInfo.entries()) {
      if (info[1][1] === undefined) {
        res.delete(info[0])
      }
    }
    return res
  }
  answer += check(R)
  while (R.size > 0) {

    // console.log('after escape move', R)
    // console.log(answer)
    R = move(R)
    // console.log('after move', R)
    // console.log('-----------------')
    answer += check(R)
    R = escape(R)
  }

  return answer
}

// console.log('result', solution(points, routes))
