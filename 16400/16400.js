const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
//const filePath = "./input.txt";
let input = fs.readFileSync(filePath).toString().trim().split("\n");

solution(input);
function solution(input) {
  let n = +input[0];
  let eratos = Array.from({ length: 40000 }, (n, i) =>
    i === 1 || i === 0 ? false : true
  );
  for (let i = 2; i < 200; i++) {
    if (eratos[i]) for (let j = 2; j < 40000 / i; j++) eratos[i * j] = false;
  }

  const dp = new Array(n + 1).fill(0);
  dp[0] = 1;
  for (let i in eratos) {
    if (eratos[i]) {
      for (let j = i; j <= n; j++) {
        dp[j] = (dp[j] + dp[j - i]) % 123456789;
      }
    }
  }
  console.log(dp[n]);
}
