#!/usr/bin/node
const { argv } = require('process');

const a = Math.floor(argv[2]);
const b = Math.floor(argv[3]);
console.log(add(a, b));

function add (a, b) {
  return a + b;
}
