const numbers = input.map(Number);
const max = Math.max(...numbers);
console.log(max);
console.log(numbers.indexOf(max) + 1);
