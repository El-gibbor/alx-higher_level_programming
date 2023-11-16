#!/usr/bin/node
const ParentSquare = require('./5-square');

class Square extends ParentSquare {
  constructor (size) {
    super(size, size);
  }

  /* 'X' as default arg when no arg is provided (undefinde) */
  charPrint (c = 'X') {
    for (let i = 0; i < this.height; i++) {
      console.log(c.repeat(this.width));
    }
  }
}

module.exports = Square;
