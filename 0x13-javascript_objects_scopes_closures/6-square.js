#!/usr/bin/node
const Rectangle = require('./4-rectangle');
module.exports = class Square extends Rectangle {
  constructor(size) {
    super(size, size);
  }

  charPrint(c) {
    if (c === undefined) {
      this.print()
    }

    else {

      for (let i = 0; i < this.height; i++) {
        let str = '';  

        for (let y = 0; y < this.width; y++) {
          str += c;

        }
        console.log(str); 
      }
  }

  }
}
