#!/usr/bin/node
const { argv } = require('process');

const allArgs = argv
console.log(allArgs.sort((a, b) => a - b).reverse()[1]);
