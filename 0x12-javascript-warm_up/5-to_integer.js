#!/usr/bin/node
const { argv } = require('process');

const toInt = Math.floor(argv[2]);
isNaN(toInt) ? console.log('Not a number') : console.log(`My number: ${argv[2]}`);
