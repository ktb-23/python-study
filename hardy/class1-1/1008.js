const solution = (a, b) => {
  let answer = a / b;
  console.log(answer.toFixed(9));
};
const [a, b] = input[0].split(" ").map(Number);
solution(a, b);
