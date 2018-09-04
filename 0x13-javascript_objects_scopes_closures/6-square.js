#!/usr/bin/node
const OldSquare = require('./5-square');
module.exports = class Square extends OldSquare {
  charPrint (c) {
    if (c === undefined) {
      this.print();
    } else {
      for (let i = 0; i < this.height; i++) {
        let str = '';

        for (let y = 0; y < this.width; y++) {
          str += c;
        }
        console.log(str);
      }
    }
  }
};
