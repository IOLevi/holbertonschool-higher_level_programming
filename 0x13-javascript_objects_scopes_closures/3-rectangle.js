#!/usr/bin/node

module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      let str = '';
      for (let y = 0; y < this.width; y++) {
        str += 'X';
      }
      console.log(str);
    }
  }
};
