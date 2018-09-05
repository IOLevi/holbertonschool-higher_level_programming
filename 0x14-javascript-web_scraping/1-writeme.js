#!/usr/bin/node

let fp = process.argv[2];
let input = process.argv[3];
let fs = require('fs');

fs.writeFile(fp, input, 'utf8', function (err) {
  if (err) {
    console.log(err);
  }
});
