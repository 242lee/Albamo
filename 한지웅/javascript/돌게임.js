const fs = require('fs');
const input = fs.readFileSync('../input.txt').toString().trim();
// const input = fs.readFileSync('/dev/stdin').toString().trim().split("\n");

input_number = Number(input);
var a = Math.floor(input_number/6);
var _a = input_number - 6 * a;
var b = Math.floor(_a/4);
var _b = _a - 4*b;
var c = Math.floor(_b/2);
var _c = _b - 2 * c;

if (_c === 0) {
    console.log('CY')
} else {
    console.log('SK')
}
