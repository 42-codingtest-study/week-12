//문제: 23048
const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
let input = fs.readFileSync(filePath).toString().trim().split("\n");

solution(input);

// for (let i = 1; i < 100; i++) {
//   solution([i]);
// }

function solution(input) {
  let n = +input[0];
  let eratos = Array.from({ length: 500000 }, (n, i) =>
    i === 1 || i === 0 ? false : true
  );
  for (let i = 2; i < 708; i++) {
    if (eratos[i]) for (let j = 2; j < 500000 / i; j++) eratos[i * j] = false;
  }
  const result = [1];
  let temp = 1;

  for (let i = 2; i <= n; i++) {
    if (eratos[i]) result.push(++temp);
    else {
      for (let j = 2; j <= i / 2; j++) {
        if (i % j == 0) {
          result.push(result[j - 1]);
          break;
        }
      }
    }
  }
  let answer = 0;
  for (let i = 1; i <= n; i++) {
    if (eratos[i]) answer++;
  }
  console.log(answer + 1);
  console.log(result.join(" "));
}
