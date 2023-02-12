const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
let input = fs.readFileSync(filePath).toString().trim().split("\n");

main(input);
function min_v(a, b) {
  return a < b ? a : b;
}

function main() {
  let n, k, l, i, tc, res;
  let cur;

  while (1) {
    const arr = input.shift();
    if (arr === undefined) break;
    [n, k] = arr.split(" ").map((x) => parseInt(x));
    if (n === -1 && k === -1) break;

    let factors = [];
    let ans = [];

    l = Math.floor(Math.sqrt(k));
    for (i = 2; i <= l; i++) {
      if (k % i === 0) {
        let t = { d: i, c: 0 };
        while (k % i === 0) {
          k = k / i;
          t.c++;
        }
        factors.push(t);
      }
    }
    if (k !== 1) factors.push({ d: k, c: 1 });
    for (let t of factors) {
      cur = t.d;
      tc = 0;
      while (cur <= n) {
        tc += Math.floor(n / cur);
        cur *= t.d;
      }
      ans.push({ d: t.d, c: min_v(t.c, tc) });
    }
    res = 1;
    for (let t of ans) {
      res *= Math.pow(t.d, t.c);
    }
    console.log(res);
  }
  return 0;
}
