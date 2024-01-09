#!/usr/bin/node
module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    } else if (w && h < 0) {
      Object.create(null);
    } else if (w && h === 0) {
      Object.create(null);
    }
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      let x = ''; /* empty str */
      for (let a = 0; a < this.width; a++) {
        x += 'X';
      }
      console.log(x);
    }
  }

  rotate () {
    [this.width, this.height] = [this.height, this.width];
  }

  double () {
    this.width = this.width * 2;
    this.height = this.height * 2;
  }
};
