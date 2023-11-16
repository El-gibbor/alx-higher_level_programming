#!/usr/bin/node

exports.converter = function (base) {
    function convertedNum (num) {
      return number.toString(base);
    }
    return convertedNum;
  };