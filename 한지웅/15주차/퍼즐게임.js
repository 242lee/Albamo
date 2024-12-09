const diffs = [1, 99999, 100000, 99995]
const times = [9999, 9001, 9999, 9001]
const limit = 	3456789012
const result = 0

// 퍼즐 풀이 조건
// diff <= level : 틀리지 않고 time_cur 만큼 시간 소요
// diff > level : diff - level 만큼 틀린다. 틀릴 때 마다 time_cur 사용하며
// 추가로 time_prev 만큼 시간을 사용해 이전 퍼즐을 다시 풀고 와야함.
// 단 이전 퍼즐을 풀 땐 틀리지 않음.
// diff - level번 틀린 이후 다시 풀면 time_cur 만큼 시간을 사용해 문제 푼다.

// 구해야 하는 것 : 최소의 숙련도로 퍼즐을 모두 풀 수 있는지 확인할 것.

// 풀이 과정
// 예시를 보니 숙련도 39354 .. ? 이를 보아하니 완전 탐색하면 터질 것으로 예상된다.
// 그렇다면, 반복문을 사용하기 보단 누적합식으로 이를 구현할 수 있지 않을까?
// 무슨 말이냐면 첫번째 문제를 풀기위한 시간, 두번째 문제를 풀기 위한 시간 (+ 첫번째 문제 풀이 시간) ...
// 아런식으로 하나하나 쌓으면 어떤데
// 내가 문제를 풀 수 있는 상황의 경우 그냥 해당 시간의 소요시간을 더하고
// 한번에 풀 수 없는 경우 diff - level을 한 Loop로 보고 한 Cycle (prev + current) 과 곱한 이후 current를 더한다.
// (Cycle * Loop) + current
// 이런 식으로 누적으로 진행하다가 아니다 싶드면 레벨을 올려서 진행!

function levelTest(diffs, times, level, limit) {
  // 현재 레벨을 입력하면, 해당 레벨에 맞춰 누적 합 연산을 진행해본다 (위의 로직)
  // 진행하면서 더이상 연산할 가치가 없다? 그러면 isEnd를 false로 그래도 두고
  // 연산이 완료된다? 그러면 숫자를 제공한다.

  // 시간을 누적하면서 리스트를 형성하려 한다.
  // 첫번째는 무조건 푸니까 일단 넣는다.
  const timeList = [times[0]]
  // 이렇게 누적하던 도중 누적합이 limit을 벗어나면 더이상 진행할 필요 없음.
  for (let i = 1; i < diffs.length; i++) {
    const pivot = level - diffs[i];
    if (pivot >= 0) {
      const latestTime = timeList[i-1] + times[i]
      if (latestTime > limit) {
        // console.log(timeList)
        return false
      }
      timeList.push(latestTime)
    } else {
      // pivot이 음수인 경우 한번에 풀이가 불가능함.
      const cycle = times[i-1] + times[i]
      // console.log('level', level, 'cycle', cycle, 'pivot', pivot)
      const latestTime = Math.abs(cycle * pivot) + timeList[i-1] + times[i]
      if (latestTime > limit) {
        //  console.log(timeList)
        return false
      }
      timeList.push(latestTime)
    }
  }
  // 위에 있는 반복문을 통과했다? 그렇다면 합격!
  // console.log(timeList)
  // console.log(timeList, limit)
  return level
}

function solution(diffs, times, limit) {
  // level을 높이며 확인하는 과정을 거칠 것이다.
  let minLev = 1;
  // 런타임 에러 발생할 수 있음. Math.max에 들어가는 값이 크다면
  // 배열의 크기가 크다면 배열 연산자의 사용을 조심해야 한다.
  let maxLev = -1;
  for (diff of diffs) {
    if (maxLev < diff) {
      maxLev = diff
    }
  }
  let ans = maxLev

  while (maxLev >= minLev) {
    const level = Math.floor((minLev + maxLev) / 2)
    const returnValue = levelTest(diffs, times, level, limit)
    if (typeof returnValue === 'number') {
      // 이 경우 연산이 되었단 말이니, 레벨을 낮출 필요성이 있다.
      ans = level
      maxLev = level - 1
    }
    else {
      minLev = level + 1
    }
  }
  return ans
}

const ans = solution(diffs, times, limit)
console.log(ans)
