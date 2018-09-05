#!/usr/bin/node

let url = process.argv[2];
let request = require('request');

request(url, (error, response, body) => {
  let res = JSON.parse(body);
  let out = {};

  if (error) {
    console.log(error);
  }

  res.forEach(item => {
    if (item['completed'] === true) {
      if (out[item['userId']]) {
        out[item['userId']] += 1;
      } else {
        out[item['userId']] = 1;
      }
    }
  });

  console.log(out);
});
