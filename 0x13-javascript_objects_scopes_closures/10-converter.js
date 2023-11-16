#!/usr/bin/node

exports.converter = function (base) {
  function convertedNum (num) {
    return num.toString(base);
  }
  return convertedNum;
};
