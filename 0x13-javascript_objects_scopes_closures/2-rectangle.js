#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (Number.isNaN(w) || w < 1 || Number.isNaN(h) || h < 1) {

    } else {
      this.width = w;
      this.height = h;
    }
  }
}
