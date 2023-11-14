#!/usr/bin/node
const { argv } = require('process');

const allArgs = argv.slice(2).map(Number);
if (allArgs.length <= 1) {
  console.log(0);
} else {
  const secondBig = allArgs.sort((a, b) => a - b).reverse()[1];
  console.log(secondBig);
}
