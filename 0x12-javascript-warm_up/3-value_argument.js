#!/usr/bin/node
const { argv } = require('process');

const msg = (argv[2] === undefined) ? 'No argument' : argv[2];
console.log(msg);
