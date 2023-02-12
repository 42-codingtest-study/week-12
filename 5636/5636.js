const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
let input = fs.readFileSync(filePath).toString().trim().split("\n");

solution(input);
function solution(input) {
  const [a, b] = input[0].split(" ").map(Number);
  let eratos = Array.from({ length: 100000 }, (n, i) =>
    i === 1 || i === 0 ? false : true
  );
  for (let i = 2; i < 317; i++) {
    if (eratos[i]) for (let j = 2; j < 100000 / i; j++) eratos[i * j] = false;
  }

  input.forEach((e) => {
    if (e === "0") return;
    const result = [];
    for (let i = 0; i < e.length; i++) {
      if (eratos[e.substr(i, 1)]) result.push(e.substr(i, 1));
      if (e.length - i > 1 && eratos[e.substr(i, 2)])
        result.push(e.substr(i, 2));
      if (e.length - i > 2 && eratos[e.substr(i, 3)])
        result.push(e.substr(i, 3));
      if (e.length - i > 3 && eratos[e.substr(i, 4)])
        result.push(e.substr(i, 4));
      if (e.length - i > 4 && eratos[e.substr(i, 5)])
        result.push(e.substr(i, 5));
    }
    console.log(Math.max(...result));
  });
}
