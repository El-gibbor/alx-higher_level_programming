#!/usr/bin/node
// computes the number of tasks completed by user id.
const r = require('request');
const uri = 'https://jsonplaceholder.typicode.com/todos';

r.get(uri, (err, res, body) => {
  if (err) {
    console.error(err);
  } else {
    const todos = JSON.parse(body);
    const tdComplete = {};

    for (const i in todos) {
      if (todos[i].completed) {
        // increments countValue of each userId in the 'completed' obj. if
        // userId does not have an existing count, it initializes the count to 1.
        tdComplete[todos[i].userId] = (tdComplete[todos[i].userId] + 1 || 1);
      }
    }
    console.log(tdComplete);
  }
});
