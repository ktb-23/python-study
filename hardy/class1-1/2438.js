const solution = (t) => {
  for (let i = 1; i <= t; i++) {
    console.log("*".repeat(i));
  }
};
const [t] = input[0].split(" ").map(Number);
solution(t);
