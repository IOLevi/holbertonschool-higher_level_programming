#!/usr/bin/node

let fp = process.argv[2];
let fs = require('fs');

fs.readFile(fp, 'utf8', function (err, data) {
  if (err) {
    console.log(err);
  } else {
    console.log(data);
  }
});
