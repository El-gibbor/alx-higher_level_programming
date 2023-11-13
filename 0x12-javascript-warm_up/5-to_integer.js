#!/usr/bin/node
const { argv } = require('process');

const toInt = Math.floor(argv[2]);
const msg = isNaN(toInt) ? 'Not a number' : toInt;
console.log(msg);
