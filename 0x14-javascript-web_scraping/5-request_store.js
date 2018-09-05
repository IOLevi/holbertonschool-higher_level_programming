#!/usr/bin/node

let url = process.argv[2];
let fp = process.argv[3];
let request = require('request');
let fs = require('fs');

request(url, (error, response, body) => {
  if (error) {
    console.log(error);
  }
  fs.writeFile(fp, body, 'utf8', function (err) {
    if (err) {
      console.log(err);
    }
  });
});
