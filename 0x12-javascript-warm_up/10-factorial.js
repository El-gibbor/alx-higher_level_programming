#!/usr/bin/node
const { argv } = require('process');

const n = Math.floor(argv[2]);
function factorial (n) {
  if (isNaN(n) || n <= 0) {
    return 1;
  } else {
    return n * factorial(n - 1);
  }
}
console.log(factorial(n));
