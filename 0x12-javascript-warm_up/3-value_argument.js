#!/usr/bin/node
const { argv } = require('process');

const msg = (argv[2] === undefined) ? 'No arguments' : argv[2];
console.log(msg);
