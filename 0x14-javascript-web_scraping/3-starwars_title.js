#!/usr/bin/node
// using star ward API, print movie title of episode matching an int

const rq = require('request');
const { argv } = require('process');
const apiEndpoint = 'https://swapi-api.alx-tools.com/api/films/' + argv[2];

rq.get(apiEndpoint, (err, resp, body) => {
  if (!err) {
    const apiData = JSON.parse(body);
    console.log(apiData.title);
  }
});
