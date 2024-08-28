const solution = (a, b) => {
  return a + b;
};
const [t] = input.shift().split(" ").map(Number);
for (let i = 0; i < t; i++) {
  const [a, b] = input.shift().split(" ").map(Number);
  console.log(solution(a, b));
}
