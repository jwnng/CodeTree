const fs = require('fs');

let input = fs.readFileSync(0).toString().trim().split(" ");

let N = Number(input[0]);

if (N < 0 &&N >= -100) {
    console.log(N);
    console.log('minus');
} else if (N > 0 && N <= 100) {
    console.log(N);
}