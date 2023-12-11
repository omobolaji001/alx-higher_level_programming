#!/usr/bin/node

function factorial (num) {
  return num === 0 || isNaN(num) ? 1 : num * factorial(num - 1);
}

const n = Number(process.argv[2]);
console.log(factorial(n));
