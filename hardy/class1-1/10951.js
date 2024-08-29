const solution = (a, b) => {
  return a + b;
};

for (let i = 0; i < input.length; i++) {
  const [a, b] = input[i].split(" ").map(Number);
  console.log(solution(a, b));
}
