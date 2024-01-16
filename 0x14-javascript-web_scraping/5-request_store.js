#!/usr/bin/node
// get and stores the content of a webpage in a file

const uri = argv[2];
const fs = require('fs');
request = require('request');
const { argv } = require('process');

request(uri, (err, response, body) => {
  if (err) {
    console.error(err);
  } else {
    fs.writeFile(argv[3], body, 'utf-8', (err) => {
      if (err) {
        console.error(err);
      }
    });
  }
});
