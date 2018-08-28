#!/usr/bin/node

if (process.argv.length === 2) {
  console.log(0);
} else if (process.argv.length === 3) {
  console.log(1);
} else {
  let a = process.argv.slice(2, process.argv.length);
  a.sort(function (a, b) { return a - b; });
  a.pop();
  console.log(a.pop());
}
