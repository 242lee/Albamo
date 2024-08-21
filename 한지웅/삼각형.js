const fs = require('fs');
const input = fs.readFileSync('../input.txt').toString().trim().split("\n");
// const input = fs.readFileSync('/dev/stdin').toString().trim().split("\n");
// input의 개행문제 제거 작업 진행
for (i = 0; i < input.length - 1; i++) {
    input[i] = input[i].trim();
    var pivot = input[i].split(' ');
    var a = Number(pivot[0]);
    var b = Number(pivot[1]);
    var c = Number(pivot[2]);

    var parse = [a,b,c]
    parse.sort()


    var y = parse[0]
    var x = parse[1]
    var z = parse[2]

    if (a + b <= c || a === 0 || b === 0 || c === 0) {
        // 우선 삼각의 자격이 아닌지 확인
        console.log('Invalid')
    } else {
        if (a === b && b === c) {
            console.log('Equilateral')
        } else if (a === b || b === c || a === c) {
            console.log('Isosceles')
        } else {
            console.log('Scalene')
        }
    }
}

