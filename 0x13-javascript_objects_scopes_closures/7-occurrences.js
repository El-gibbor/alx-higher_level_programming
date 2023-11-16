#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  return list.filter((x) => x === searchElement).length;
};
