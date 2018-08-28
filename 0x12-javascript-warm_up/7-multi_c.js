#!/usr/bin/node
let x = process.argv[2];

if (Number.isNaN(parseInt(x))) {
  console.log('Missing number of occurences');
} else {
  for (let i = 0; i < parseInt(x); i++) {
    console.log('C is fun');
  }
}
