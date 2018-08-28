#!/usr/bin/node
let x = parseInt(process.argv[2]);
if (Number.isNaN(x)) {
  console.log('Missing size');
} else {
  let str = '';
  for (let i = 0; i < x; i++) {
    str = '';
    for (let j = 0; j < x; j++) {
      str += 'x';
    }
    console.log(str);
  }
}
