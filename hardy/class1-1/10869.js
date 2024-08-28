const solution = (a, b) => {
  console.log(a + b);
  console.log(a - b);
  console.log(a * b);
  console.log(parseInt(a / b));
  console.log(a % b);
};
const [a, b] = input[0].split(" ").map(Number);
solution(a, b);
