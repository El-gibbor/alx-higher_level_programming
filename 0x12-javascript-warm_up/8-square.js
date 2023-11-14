#!/usr/bin/node
const { argv } = require('process');

const x = Math.floor(argv[2]); // convertible to an int
if (isNaN(x)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < x; i++) {
    let Xsqr = '';
    for (let j = 0; j < x; j++) {
      Xsqr += 'X';
    }
    console.log(Xsqr);
  }
}
