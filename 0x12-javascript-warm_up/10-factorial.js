#!/usr/bin/node
let a = parseInt(process.argv[2]);

function fact (a) {
  if (Number.isNaN(a)) {
    return 1;
  } else if (a === 1 || a === 0) {
    return 1;
  }

  return a * fact(a - 1);
}

console.log(fact(a));
