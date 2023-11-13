#!/usr/bin/node
const { argv } = require('process');

const x = argv.length;
const msg = (x < 3) ? 'No argument' : (x === 3) ? 'Argument found' : 'Arguments found';
console.log(msg);
