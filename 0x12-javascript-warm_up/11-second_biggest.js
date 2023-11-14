#!/usr/bin/node
const { argv } = require('process');

const allArgs = argv.slice(2).map(Number); // new array with its elements casted to int
if (allArgs.length <= 1) {
    console.log(0);
} else {
    const secondBig = allArgs.sort((a, b) => a - b).reverse()[1];
    console.log(secondBig);
}
/* sort() takes a comparison function that defines the sort order. The return value is a
 number that indicate the relative order of the two elements: negative if a is less than b,
 positive if a is greater than b, and zero if they are equal. without this comparison, the
 array is sorted as a string which wouldnt be correct when you are expecting a numeric sort.
*/
