const [t] = input.shift().split(" ").map(Number);
const numbers = input[0].split(" ").map(Number);
console.log(Math.min(...numbers), Math.max(...numbers));
