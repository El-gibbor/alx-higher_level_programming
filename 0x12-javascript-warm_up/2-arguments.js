#!/usr/bin/node
const { argv } = require('process');

const msg = (argv.length < 3) ? 'No argument' : (argv.length === 3) ? 'Argument found' : 'Arguments found';
console.log(msg);
