const solution = (a, b) => {
  return a + b;
};
let i = 0;
for (;;) {
  const [a, b] = input[i].split(" ").map(Number);
  if (a == 0 && b == 0) break;
  console.log(solution(a, b));
  i++;
}
