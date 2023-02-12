//문제: 3671
const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
let input = fs.readFileSync(filePath).toString().trim().split("\n");

solution(input);
function solution(input) {
  let n = +input.shift();

  let eratos = Array.from({ length: 9999999 }, (n, i) =>
    i === 1 || i === 0 ? false : true
  );
  for (let i = 2; i < 3162; i++) {
    if (eratos[i]) for (let j = 2; j < 9999999 / i; j++) eratos[i * j] = false;
  }

  const getPermutations = function (arr, selectNumber) {
    const results = [];
    if (selectNumber === 1) return arr.map((el) => [el]);
    // n개중에서 1개 선택할 때(nP1), 바로 모든 배열의 원소 return. 1개선택이므로 순서가 의미없음.

    arr.forEach((fixed, index, origin) => {
      const rest = [...origin.slice(0, index), ...origin.slice(index + 1)];
      // 해당하는 fixed를 제외한 나머지 배열
      const permutations = getPermutations(rest, selectNumber - 1);
      // 나머지에 대해서 순열을 구한다.
      const attached = permutations.map((el) => [fixed, ...el]);
      //  돌아온 순열에 떼 놓은(fixed) 값 붙이기
      results.push(...attached);
      // 배열 spread syntax 로 모두다 push
    });

    return results; // 결과 담긴 results return
  };

  input.forEach((data) => {
    let result = 0;
    const result_arr = [];
    const arr = data.split("");
    for (let i = 1; i <= arr.length; i++) {
      for (let k of getPermutations(arr, i)) {
        if (eratos[+k.join("")]) {
          if (!result_arr.includes(+k.join(""))) {
            result_arr.push(+k.join(""));
            result++;
          }
        }
      }
    }
    console.log(result);
  });
}
