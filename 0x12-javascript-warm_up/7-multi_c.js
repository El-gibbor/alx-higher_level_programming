#!/usr/bin/node
const { argv } = require('process');

const x = Math.floor(argv[2]); // convertible to an int
if (isNaN(x)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < x; i++) {
    console.log('C is fun');
  }
}
