const [t] = input.shift().split(" ").map(Number);

const result = input[0]
  .split("")
  .map(Number)
  .reduce((acc, cur) => parseInt((acc += cur)), 0);
console.log(result);
