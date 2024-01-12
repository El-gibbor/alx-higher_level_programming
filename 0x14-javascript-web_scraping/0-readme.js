#!/usr/bin/node
// reads and prints the content of a file.

const fs = require('node:fs');
const { argv } = require('process');

fs.readFile(argv[2], 'utf-8', (error, data) => {
    if (error) {
        console.error(error);
    } else {
        console.log(data);
    }
});
