#!/usr/bin/node
// Displays status code of a Get request

const rq = require('request');
const { argv } = require('process');

rq.get(argv[2], (err, res, body) => {
  if (!err) {
    console.log(`code: ${res.statusCode}`);
  }
});
